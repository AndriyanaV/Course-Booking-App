import {ref } from 'vue'

export function useUserRole(){
  const userRole = ref(null);

  const checkUserRole = () => {
    const role = localStorage.getItem("rola");
    userRole.value = role;
    // console.log(userRole.value)
    
};



return {
    userRole,
    checkUserRole
}; 
}