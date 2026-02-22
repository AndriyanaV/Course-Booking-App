import * as yup from "yup";

export const loginSchema = (imagePreview) => {
  return yup.object({
    email: yup
      .string()
      .required("Please enter your email")
      .email("Invalid email format"),
    password: yup.string().required("Please enter your password"),
  });
};
