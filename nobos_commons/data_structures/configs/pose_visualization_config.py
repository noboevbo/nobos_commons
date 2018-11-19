class PoseVisualizationConfig(object):
    __slots__ = ['min_human_score_to_show', 'min_limb_score_to_show', 'min_joint_score_to_show']

    def __init__(self):
        self.min_human_score_to_show = 0.8
        self.min_limb_score_to_show = 0.8
        self.min_joint_score_to_show = 0.8
