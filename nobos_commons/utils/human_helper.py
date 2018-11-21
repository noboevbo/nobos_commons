from collections import defaultdict
from typing import Dict, List

from nobos_commons.data_structures.human import HumanPoseResult, Limb2D


def is_joint_from_limb_in_human(human: HumanPoseResult, limb_candidate: Limb2D) -> bool:
    return human.joints[limb_candidate.joint_from.num] == limb_candidate.joint_from or \
           human.joints[limb_candidate.joint_to.num] == limb_candidate.joint_to


def get_empty_human(num_joints, num_limbs) -> HumanPoseResult:
    human = HumanPoseResult([None] * num_joints, [None] * num_limbs, 0)
    return human


def are_joints_in_both_humans(human_a: HumanPoseResult, human_b: HumanPoseResult) -> bool:
    for joint_idx, joint in enumerate(human_b.joints):
        if joint is not None and human_a.joints[joint_idx] is not None:
            return True
    return False


def get_merged_humans(human_a: HumanPoseResult, human_b: HumanPoseResult) -> HumanPoseResult:
    for joint_idx, joint in enumerate(human_b.joints):
        if joint is None:
            continue
        if human_a.joints[joint_idx] is not None:
            raise RuntimeError("Merge conflict, joint exists in both humans")
        human_a.joints[joint_idx] = joint

    for limb_idx, limb in enumerate(human_b.limbs):
        if limb is None:
            continue
        if human_a.limbs[limb_idx] is not None:
            raise RuntimeError("Merge conflict, limb exists in both humans")  #
        human_a.limbs[limb_idx] = limb

    human_a.score += human_b.score
    return human_a


def get_humans_from_limbs(limbs: Dict[int, List[Limb2D]], skeleton_config: SkeletonConfigBase, min_number_of_limbs: int,
                          min_human_score: float) -> (List[HumanPoseResult], Dict[int, List[Limb2D]]):
    # last number in each row is the total parts number of that person
    # the second last number in each row is the score of the overall configuration
    human_list: List[HumanPoseResult] = []  # Humans n, 20
    limbs_used: List[Limb2D] = []

    for limb_nr, limb_candidates in limbs.items():
        for i, limb_candidate in enumerate(limb_candidates):
            found = 0
            subset_idx = [-1, 1]
            for j in range(len(human_list)):
                if is_joint_from_limb_in_human(human_list[j], limb_candidate):
                    subset_idx[found] = j
                    found += 1
            if found == 1:
                j = subset_idx[0]
                if human_list[j].joints[limb_candidate.joint_to.num] != limb_candidate.joint_to:
                    human_list[j].joints[limb_candidate.joint_to.num] = limb_candidate.joint_to
                    human_list[j].limbs[limb_candidate.num] = limb_candidate
                    if limb_candidate not in limbs_used:
                        limbs_used.append(limb_candidate)
                    human_list[j].score += limb_candidate.score + limb_candidate.joint_to.score

            elif found == 2:
                j1, j2 = subset_idx
                # print("found = 2")
                if not are_joints_in_both_humans(human_list[j1], human_list[j2]):
                    human_list[j1] = get_merged_humans(human_list[j1], human_list[j2])
                    del human_list[j2]
                else:  # as like found == 1
                    human_list[j1].joints[limb_candidate.joint_to.num] = limb_candidate.joint_to
                    human_list[j1].limbs[limb_candidate.num] = limb_candidate
                    if limb_candidate not in limbs_used:
                        limbs_used.append(limb_candidate)
                    human_list[j1].score += limb_candidate.score + limb_candidate.joint_to.score
            elif not found:
                human = get_empty_human(len(skeleton_config.joints), len(skeleton_config.limbs))
                human.joints[limb_candidate.joint_from.num] = limb_candidate.joint_from
                human.joints[limb_candidate.joint_to.num] = limb_candidate.joint_to
                human.limbs[limb_candidate.num] = limb_candidate
                if limb_candidate not in limbs_used:
                    limbs_used.append(limb_candidate)
                human.score = limb_candidate.matched_score
                human_list.append(human)

    # Remove humnans which have too low number of limbs or a too low total limb score.
    # cfg.pose_estimator.skeleton_limb_score
    # cfg.pose_estimator.skeleton_min_limbs
    deleteIdx = []
    for i in range(len(human_list)):
        if human_list[i].num_limbs < min_number_of_limbs or (human_list[i].score / human_list[i].num_limbs) < min_human_score:
            deleteIdx.append(i)
    humans = [x for i, x in enumerate(human_list) if i not in deleteIdx]

    # Collect limbs which aren't contained in a human, TODO: DOESNT INCLUDE THE ONES FROM DELETE HUMANS!
    straying_limbs: Dict[int, List[Limb2D]] = defaultdict(list)
    for limb_num, limb_list in limbs.items():
        for limb in limb_list:
            if limb not in limbs_used:
                straying_limbs[limb_num].append(limb)

    return humans, straying_limbs