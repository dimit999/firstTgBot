import allure
from PIL import Image, ImageEnhance, ImageFilter


class TransformImageSteps:

    @staticmethod
    def transform_image(filename):
        with allure.step("Read image using Image.open"):
            source_image = Image.open(filename)

        with allure.step("Use filters: ImageFilter.EMBOSS. "
                         "Existing filters: BLUR/CONTOUR/DETAIL/EDGE_ENHANCE/EDGE_ENHANCE_MORE/EMBOSS/"
                         "FIND_EDGES/SHARPEN/SMOOTH/SMOOTH_MORE"):
            enhanced_image = source_image.filter(ImageFilter.EMBOSS)

        with allure.step("Convert image RGBA to RGB for saving to JPEG "):
            enhanced_image = enhanced_image.convert('RGB')

        with allure.step("Save image"):
            enhanced_image.save(filename)

        return filename
