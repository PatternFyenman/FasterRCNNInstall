#inherits a base config
_base_='../faster_rcnn/faster_rcnn_r50_fpn_1x_coco.py'

#change the num_classes in head to match the dataset's annotation
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=2)))

#modify dataset related settings
dataset_type = 'COCODataset'
classes = ('library','diplo',)
data = dict(
    train=dict(
        img_prefix='/home/pattern/Downloads/mmdetection-2.7.0/data/coco/train2017/',
        classes=classes,
        ann_file='/home/pattern/Downloads/mmdetection-2.7.0/data/coco/annotations/instances_train2017.json'),
    val=dict(
        img_prefix='/home/pattern/Downloads/mmdetection-2.7.0/data/coco/val2017/',
        classes=classes,
        ann_file='/home/pattern/Downloads/mmdetection-2.7.0/data/coco/annotations/instances_val2017.json'),
    test=dict(
        img_prefix='/home/pattern/Downloads/mmdetection-2.7.0/data/coco/val2017/',
        classes=classes,
        ann_file='/home/pattern/Downloads/mmdetection-2.7.0/data/coco/annotations/instances_val2017.json'))

#use the [re-trained faster-rcnn model to obtain higher pweformance
#load_from = '/home/pattern/Downloads/mmdetection-2.7.0/checkpoints/faster_rcnn_r50_fpn_1x_coco_20200130-047c8118.pth'
