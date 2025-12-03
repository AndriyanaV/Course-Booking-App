import { defineStore } from "pinia";
import { ref } from "vue";

export const useUserStore = defineStore("user", () => {
  const userRole = ref(null);
  const userId = ref(null);
  const accessToken = ref(null);
  const isLoggedIn = ref(false);
  const showLogoutPopUp = ref(false);

  // After login
  const setUser = ({ role, user_id, token }) => {
    userRole.value = role;
    userId.value = user_id;
    accessToken.value = token;
    isLoggedIn.value = true;

    // Local set
    const expirationTime = Date.now() + 3 * 24 * 60 * 60 * 1000; // 3 dana
    localStorage.setItem("access_token", token);
    localStorage.setItem("token_expiration", expirationTime.toString());
    localStorage.setItem("rola", role);
    localStorage.setItem("user_id", user_id);
  };

  const logout = () => {
    userRole.value = null;
    userId.value = null;
    accessToken.value = null;
    isLoggedIn.value = false;
    showLogoutPopUp.value = false;

    localStorage.removeItem("access_token");
    localStorage.removeItem("token_expiration");
    localStorage.removeItem("rola");
    localStorage.removeItem("user_id");
  };

  const initFromStorage = () => {
    const token = localStorage.getItem("access_token");
    const role = localStorage.getItem("rola");
    const user_id = localStorage.getItem("user_id");
    const expiration = Number(localStorage.getItem("token_expiration") || 0);

    if (token && role && user_id && Date.now() < expiration) {
      userRole.value = role;
      userId.value = user_id;
      accessToken.value = token;
      isLoggedIn.value = true;
    }
  };

  //Manage Logout Pop Up
  const toggleLogoutPopUp = () => {
    showLogoutPopUp.value = !showLogoutPopUp.value;
  };

  return {
    userRole,
    userId,
    accessToken,
    isLoggedIn,
    showLogoutPopUp,
    setUser,
    logout,
    initFromStorage,
    toggleLogoutPopUp
  };
});
