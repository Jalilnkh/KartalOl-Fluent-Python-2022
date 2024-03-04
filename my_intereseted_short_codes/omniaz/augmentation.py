from pathlib import Path, PurePosixPath
import cv2
from torchvision import transforms as TF


class Augmentation:
    def __init__(
        self,
        ref_path,
        brightness_1=0.5,
        hue_1=0.1,
        brightness_2=0.2,
        hue_2=0.3,
        quality_lower=20,
    ):
        self.ref_path = ref_path
        self.brightness_1 = brightness_1
        self.hue_1 = hue_1
        self.brightness_2 = brightness_2
        self.hue_2 = hue_2
        self.quality_lower = quality_lower

    def get_images(self):
        images_info = []
        for SKU_paths in list(Path(self.ref_path + "/output").iterdir()):
            for file_path in list(Path(SKU_paths).iterdir()):
                images_info.append([cv2.imread(str(file_path)), SKU_paths, file_path])
        return images_info

    def apply_functions(self, images_info):
        for image_info, i in zip(images_info, range(len(images_info))):
            jitter = TF.ColorJitter(brightness=self.brightness_1, hue=self.hue_1)
            augmented_image = jitter(image_info[0])
            img_name = "_".join(str(x) for x in ["_aug_RBC_", i, ".jpg"])
            cv2.imwrite(
                str(image_info[1] / PurePosixPath(str(image_info[2])).name / img_name),
                augmented_image,
            )
            jitter = TF.ColorJitter(brightness=self.brightness_2, hue=self.hue_2)
            augmented_image = jitter(image_info[0])
            img_name = "_".join(str(x) for x in ["_aug_RBCvs_", i, ".jpg"])
            cv2.imwrite(
                str(image_info[1] / PurePosixPath(str(image_info[2])).name / img_name),
                augmented_image,
            )
            rotater = TF.RandomRotation(degrees=(0, 30))
            augmented_image = rotater(image_info[0])
            img_name = "_".join(str(x) for x in ["_aug_Rotate_15_", i, ".jpg"])
            cv2.imwrite(
                str(image_info[1] / PurePosixPath(str(image_info[2])).name / img_name),
                augmented_image,
            )
            perspective_transformer = TF.RandomPerspective(distortion_scale=0.4, p=1.0)
            augmented_image = perspective_transformer(image_info[0])
            img_name = "_".join(str(x) for x in ["_aug_resp_", i, ".jpg"])
            cv2.imwrite(
                str(image_info[1] / PurePosixPath(str(image_info[2])).name / img_name),
                augmented_image,
            )
