/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      animation: {
        shake: "shake 0.5s linear infinite",
      },
      keyframes: {
        shake: {
          "0%, 100%": { transform: "translateX(0)" },
          "25%": { transform: "translateX(-5px)" },
          "75%": { transform: "translateX(5px)" },
        },
      },
      width: {
        mainPage: "1280px",
        card: "333px",
        userCard: "140px",
      },
      height: {
        card: "101px",
        userCard: "40px",
      },
    },
  },
  plugins: [],
};
