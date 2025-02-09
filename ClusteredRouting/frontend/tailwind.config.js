/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",  // Add your project files here
    "./public/index.html",          // HTML files (optional)
  ],
  theme: {
    extend: {
      colors: {
        primary: "#3490dc",          // Custom color example
        secondary: "#ffed4a",        // Custom color example
        danger: "#e3342f",           // Custom color example
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'], // Example of custom font
      },
      spacing: {
        128: '32rem',                // Custom spacing size example
        144: '36rem',                // Custom spacing size example
      },
    },
  },
  plugins: [],
}
