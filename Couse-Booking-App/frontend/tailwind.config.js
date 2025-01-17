/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html", // Ako imate index.html
    "./src/**/*.{vue,js,ts,jsx,tsx}" // Putanje do Vue i JS fajlova
  ],
  safelist: [
    {
      pattern: /text-(blue|green|indigo|pink|orange|rose)-(600|400)/,
      variants: ['hover'],
    }
  ],
  
  theme: {
    extend: {
      fontFamily: {
        gilroy: ['Gilroy', 'sans-serif'],
      },
      fontSize: {
        'h1': '70px', 
      },
      boxShadow: {
        custom: '0 0px 3px rgba(0, 0, 0, 0.25)', // Prilagođena senka
      },
      
    },
  },
  plugins: [],
}

