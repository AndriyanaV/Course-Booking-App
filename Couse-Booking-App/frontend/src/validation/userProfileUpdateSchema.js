import * as yup from "yup";

export const userProfileUpdateSchema = (imagePreview) => {
  return yup.object({
    firstName: yup.string().required("First name is required"),
    lastName: yup.string().required("Last name is required"),
    email: yup.string().email().required("Email is required"),
    phoneNumber: yup.string().nullable(),
    image: yup
      .mixed()
      .nullable()
      .test("no-required", function (value) {
        if (value) return true;
        if (imagePreview.value) return true;
        return true;
      })
      .test("fileType", "Only PNG and JPEG images are allowed", (file) => {
        if (!file) return true;
        return ["image/png", "image/jpeg"].includes(file.type);
      })
      .test("fileSize", "Image must be under 2MB", (file) => {
        if (!file) return true;
        return file.size <= 2 * 1024 * 1024;
      }),
  });
};
