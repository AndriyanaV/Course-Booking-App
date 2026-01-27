<template>
  <div class="lg:w-[500px] flex flex-col gap-[40px]">
    <div class="user-form-container w-full">
      <Form :validation-schema="schema" :initial-values="initialValues" @submit="handleLogin" class="w-full flex flex-col gap-[20px]">
        <!-- Server message -->
        <div v-if="serverMessage" class="w-full h-fit flex items-center gap-[16px] text-gray-600">
          <div class="w-1/2 flex flex-col gap-2">
            <h4 class="m-0 font-bold">HMM!</h4>
            <p>{{ serverMessage }}</p>
          </div>
          <div class="w-1/2 h-[140px] flex flex-col gap-2">
            <img src="/images/emoji.png" class="w-full h-full object-contain" />
          </div>
        </div>

        <h1 class="text-xl leading-tight tracking-tight text-medium-purple md:text-2xl font-bold">
          Sign in to your account
        </h1>

        <!--Email -->
        <div class="flex flex-col gap-[12px]">
          <label for="email" class="block mb-2 text-base font-medium text-dark-purple">Email</label>
          <Field name="email" type="text" placeholder="myemail@gmail.com" class="input-el" />
          <ErrorMessage name="email" class="error-message" />
        </div>

        <!-- Password-->
        <div class="flex flex-col gap-[12px]">
          <label for="password" class="block text-base font-medium text-dark-purple">Password</label>
          <Field name="password" type="password" placeholder="••••••••" class="input-el" />
          <ErrorMessage name="password" class="error-message" />
        </div>

        <div class="w-full flex flex-col gap-[10px]">
          <button type="submit" class="w-full !mt-[10px] text-white bg-gradient-to-br from-[#7786EB] to-[#7786EB] 
                   hover:to-[#7F8BF0] transition-all duration-500 ease-in-out 
                   focus:outline-none focus:ring-primary-300 font-bold rounded-[10px] text-[16px] px-5 py-2.5 text-center capitalize">
            Sign in
          </button>
          <p class="text-sm font-light text-gray-500">
            Don’t have an account yet?
            <a href="#" class="font-medium text-primary-600 hover:underline !hover:bg-none">Sign up</a>
          </p>
        </div>
      </Form>
    </div>
  </div>
</template>

<script setup>
import { Form, Field, ErrorMessage } from "vee-validate";
import * as yup from "yup";
import { loginSchema } from "@/validation/loginSchema.js";

const props = defineProps({
  serverMessage: { type: String, default: null },
});

const emit = defineEmits(["login"]);

// validation schema
const schema = loginSchema();


// initial values
const initialValues = {
  email: "",
  password: "",
};

// submit 
const handleLogin = (values) => {
  emit("login", values);
};
</script>

<style>

</style>
