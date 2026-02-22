import { ref } from 'vue';

export function useConfirmCard() {
  const confirmCard = ref(false);  

  // State of confirmCard
  const toggleConfirmCard = () => {
    confirmCard.value = !confirmCard.value;  
  };

  return {
    confirmCard,   
    toggleConfirmCard, 
  };
}
