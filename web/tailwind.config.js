/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html", // Ako imate index.html
    "./src/**/*.{vue,js,ts,jsx,tsx}", // Putanje do Vue i JS fajlova
  ],
  safelist: [
    {
      pattern: /text-(blue|green|indigo|pink|orange|rose)-(600|400)/,
      variants: ["hover"],
    },
  ],

  theme: {
    extend: {
      fontFamily: {
        poppins: ["Poppins", "sans-serif"],
      },
      fontSize: {
        h1: "70px",
      },
      boxShadow: {
        custom: "0 0px 3px rgba(0, 0, 0, 0.25)", // Prilagođena senka
      },
      colors: {
        "main-blue": "#2D3CFF", 
        "second-blue": "#3b82f6",
        "light-purple":"#886df6",
        "soft-blue":"#E6EDFE",
        "language-heading":"#46A5BA",
        "button-main-color":"#46A5BA",
        "medium-purple": "#7786EB",
        "dark-purple":"#474E84"
      },
    },
  },
  plugins: [],
};
