//Create-react-app config override
module.exports = {
	style: {
		postcss: {
			plugins: [
				require('tailwindcss'),
				require('autoprefixer')
			]
		}
	}
}
