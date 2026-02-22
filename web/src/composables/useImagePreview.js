import { ref, onUnmounted } from "vue";

export function useImagePreview() {
  const preview = ref(null);

  const setFile = (file) => {
    if (!file) return;

    if (preview.value?.startsWith("blob:")) {
      URL.revokeObjectURL(preview.value);
    }

    preview.value = URL.createObjectURL(file);
  };

  onUnmounted(() => {
    if (preview.value?.startsWith("blob:")) {
      URL.revokeObjectURL(preview.value);
    }
  });

  return {
    preview,
    setFile,
  };
}
