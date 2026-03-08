import * as yup from "yup";

export const userProfileUpdateSchema = (imagePreview, userRole) => {
  return yup.object({
    firstName: yup.string().required("First name is required"),
    lastName: yup.string().required("Last name is required"),
    phoneNumber: yup.string().nullable(),
    image: yup
      .mixed()
      .nullable()
      .test("required-if-professor", "Profile image is required", function (value) {
        if (userRole === "professor") {
          // we need image for professor
          return !!value || !!imagePreview.value;
        }
        return true;
      })
      .test("fileType", "Only PNG and JPEG images are allowed", (file) => {
        if (!file) return true;
        return ["image/png", "image/jpeg"].includes(file.type);
      })
      .test("fileSize", "Image must be under 5MB", (file) => {
        if (!file) return true;
        return file.size <= 5 * 1024 * 1024;
      }),
  });
};
