import { useUserStore } from "@/stores/user";
import router from "@/router";
import { toast } from "vue3-toastify";

export function useLogout() {
  const userStore = useUserStore();

  const logout = () => {
    userStore.logout(); //from user store
    router
      .push("/")
      .then(() => toast.success("You have successfully logged out!"));
  };

  return { logout };
}
