/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html", // Ako imate index.html
    "./src/**/*.{vue,js,ts,jsx,tsx}" // Putanje do Vue i JS fajlova
  ],
  theme: {
    extend: {
      fontFamily: {
        gilroy: ['Gilroy', 'sans-serif'],
      },
    },
  },
  plugins: [],
}

