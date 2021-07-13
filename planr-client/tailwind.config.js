module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],		//Remove unused styles from tailwind
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {},
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
