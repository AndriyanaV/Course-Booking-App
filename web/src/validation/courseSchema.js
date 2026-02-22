import * as yup from "yup";

export const courseSchema = (imagePreviewRef) =>
  yup.object({
    name: yup.string().required("Course name is required"),
    language: yup.string().required("Language is required"),
    image: yup
      .mixed()
      .nullable()
      .test("required-if-no-preview", "Image is required", function (file) {
        if (file) return true; // new file chosen
        if (imagePreviewRef.value) return true; // if we have preview image (edit mode)
        return false; // no image 
      })
      .test("fileType", "Only PNG and JPEG images are allowed", (file) => {
        if (!file) return true;
        return ["image/png", "image/jpeg"].includes(file.type);
      })
      .test("fileSize", "Image size should not exceed 2MB", (file) => {
        if (!file) return true;
        return file.size <= 2 * 1024 * 1024;
      }),
  });
