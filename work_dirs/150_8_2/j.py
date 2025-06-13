model = dict(
    type='RecognizerGCN',
    backbone=dict(
        type='STGCN',
        gcn_adaptive='init',
        gcn_with_res=True,
        tcn_type='mstcn',
        graph_cfg=dict(layout='drive_behavior', mode='spatial')),
    cls_head=dict(type='GCNHead', num_classes=11, in_channels=256))
dataset_type = 'PoseDataset'
ann_file = 'training_file/2025_1_14.pkl'
train_pipeline = [
    dict(type='PreNormalize3D'),
    dict(type='GenSkeFeat', dataset='drive_behavior', feats=['j']),
    dict(type='UniformSample', clip_len=150),
    dict(type='PoseDecode'),
    dict(type='FormatGCNInput', num_person=1),
    dict(type='Collect', keys=['keypoint', 'label'], meta_keys=[]),
    dict(type='ToTensor', keys=['keypoint'])
]
val_pipeline = [
    dict(type='PreNormalize3D'),
    dict(type='GenSkeFeat', dataset='drive_behavior', feats=['j']),
    dict(type='UniformSample', clip_len=150, num_clips=3),
    dict(type='PoseDecode'),
    dict(type='FormatGCNInput', num_person=1),
    dict(type='Collect', keys=['keypoint', 'label'], meta_keys=[]),
    dict(type='ToTensor', keys=['keypoint'])
]
test_pipeline = [
    dict(type='PreNormalize3D'),
    dict(type='GenSkeFeat', dataset='drive_behavior', feats=['j']),
    dict(type='UniformSample', clip_len=150, num_clips=15),
    dict(type='PoseDecode'),
    dict(type='FormatGCNInput', num_person=1),
    dict(type='Collect', keys=['keypoint', 'label'], meta_keys=[]),
    dict(type='ToTensor', keys=['keypoint'])
]
data = dict(
    videos_per_gpu=16,
    workers_per_gpu=2,
    test_dataloader=dict(videos_per_gpu=1),
    train=dict(
        type='RepeatDataset',
        times=5,
        dataset=dict(
            type='PoseDataset',
            ann_file='training_file/2025_1_14.pkl',
            pipeline=[
                dict(type='PreNormalize3D'),
                dict(type='GenSkeFeat', dataset='drive_behavior', feats=['j']),
                dict(type='UniformSample', clip_len=150),
                dict(type='PoseDecode'),
                dict(type='FormatGCNInput', num_person=1),
                dict(type='Collect', keys=['keypoint', 'label'], meta_keys=[]),
                dict(type='ToTensor', keys=['keypoint'])
            ],
            split='xsub_train')),
    val=dict(
        type='PoseDataset',
        ann_file='training_file/2025_1_14.pkl',
        pipeline=[
            dict(type='PreNormalize3D'),
            dict(type='GenSkeFeat', dataset='drive_behavior', feats=['j']),
            dict(type='UniformSample', clip_len=150, num_clips=3),
            dict(type='PoseDecode'),
            dict(type='FormatGCNInput', num_person=1),
            dict(type='Collect', keys=['keypoint', 'label'], meta_keys=[]),
            dict(type='ToTensor', keys=['keypoint'])
        ],
        split='xsub_val'),
    test=dict(
        type='PoseDataset',
        ann_file='training_file/2025_1_14.pkl',
        pipeline=[
            dict(type='PreNormalize3D'),
            dict(type='GenSkeFeat', dataset='drive_behavior', feats=['j']),
            dict(type='UniformSample', clip_len=150, num_clips=15),
            dict(type='PoseDecode'),
            dict(type='FormatGCNInput', num_person=1),
            dict(type='Collect', keys=['keypoint', 'label'], meta_keys=[]),
            dict(type='ToTensor', keys=['keypoint'])
        ],
        split='xsub_val'))
optimizer = dict(
    type='SGD', lr=0.005, momentum=0.9, weight_decay=0.0005, nesterov=True)
optimizer_config = dict(grad_clip=None)
lr_config = dict(policy='CosineAnnealing', min_lr=0, by_epoch=False)
total_epochs = 120
checkpoint_config = dict(interval=1)
evaluation = dict(interval=1, metrics=['top_k_accuracy'])
log_config = dict(interval=100, hooks=[dict(type='TextLoggerHook')])
log_level = 'INFO'
work_dir = './work_dirs/150_8_2'
gpu_ids = [0]
