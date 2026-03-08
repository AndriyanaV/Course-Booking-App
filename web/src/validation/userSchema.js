import * as yup from "yup";
import { countryCodes } from "@/constants/countryCode";

export const userSchema = (isAddMode, imagePreviewRef, selectedCountryCodeRef) =>
  yup.object({
    firstName: yup.string().required("First name is required"),
    lastName: yup.string().required("Last name is required"),

    email: yup
      .string()
      .email("Invalid email format")
      .required("Email is required"),

    phoneNumber: yup
      .string()
      .nullable()
      .transform(function (value) {
        // value = lokalni broj iz inputa
        if (!value) return null;
        // prefiks iz selecta
        const prefix = selectedCountryCodeRef.value || "";
        return prefix + value.replace(/\D/g, ""); // ukloni eventualne razmake/znakove
      })
      .test("phone-validation", "Invalid phone number", function (value) {
        if (!value) return true; // prazno je ok
        const country = countryCodes.find((c) => value.startsWith(c.code));
        if (!country) return false;
        return country.regex.test(value);
      }),

    role: yup
      .string()
      .oneOf(["user", "professor", "admin"], "Invalid role")
      .required("Role is required"),

    // ADD vs EDIT
    password: isAddMode
      ? yup
          .string()
          .required("Password is required")
          .min(6, "Password must be at least 6 characters")
      : yup.string().notRequired(),

    retypePassword: isAddMode
      ? yup
          .string()
          .required("Please confirm password")
          .oneOf([yup.ref("password")], "Passwords do not match")
      : yup.string().notRequired(),

    biography: yup.string().when("role", {
      is: "professor",
      then: (schema) =>
        schema
          .required("Biography is required for professors")
          .max(500, "Biography can be max 500 characters"),
      otherwise: (schema) => schema.notRequired(),
    }),

    image: yup
      .mixed()
      .nullable()
      .test(
        "required-if-professor",
        "Image is required for professors",
        function (file) {
          const role = this.parent.role;

          // Ako nije professor → slika nije obavezna
          if (role !== "professor") return true;

          // Ako je professor:
          // 1. ako je uploadovao novu sliku
          if (file) return true;

          // 2. ako postoji preview (edit mode)
          if (imagePreviewRef.value) return true;

          // 3. nema ni file ni preview → greška
          return false;
        },
      )
      .test("fileType", "Only PNG and JPEG images are allowed", (file) => {
        if (!file) return true;
        return ["image/png", "image/jpeg"].includes(file.type);
      })
      .test("fileSize", "Image size should not exceed 5MB", (file) => {
        if (!file) return true;
        return file.size <= 5 * 1024 * 1024;
      }),
  });
