/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      width: {
        mainPage: "1280px",
        card: "371px",
        userCard: "140px",
      },
      height: {
        card: "113px",
        userCard: "40px",
      },
    },
  },
  plugins: [],
};
