import * as yup from "yup";

export const currentCourseSchema = () => {
  return yup.object({
    price: yup
      .number()
      .transform((value, originalValue) =>
        originalValue === "" ? undefined : value,
      )
      .typeError("Price must be a number") // kad neko unese npr. "abc"
      .positive("Price must be positive")
      .required("Price is required"),
    maxMembers: yup
      .number()
      .typeError("Max members must be a number")
      .integer("Max members must be an integer")
      .positive("Max members must be positive")
      .required("Max members is required"),
    startAt: yup
      .date()
      .typeError("Start date is required")
      .required("Start date is required"),
    endAt: yup
      .date()
      .typeError("End date is required")
      .min(yup.ref("startAt"), "End date cannot be before start date")
      .required("End date is required"),
    location: yup.string().required("Location is required"),
    lessons: yup
      .number()
      .typeError("Number of lessons must be a number")
      .integer("Number of lessons must be an integer")
      .positive("Number of lessons must be positive")
      .required("Number of lessons is required"),
    level: yup
      .string()
      .oneOf(
        ["beginner", "intermediate", "advanced"],
        "Please choose a valid level",
      )
      .required("Level is required"),
    professor: yup.string().required("Professor is required"),
  });
};
