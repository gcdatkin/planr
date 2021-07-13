
function Button(props) {

    return (
        // <div className="Button border border-gray-200">
            <button className="p-2 border border-gray-200 rounded bg-gray-100 hover:bg-gray-200 active:bg-gray-300 transition-colors duration-75">{props.value || "Button"}</button>
        // </div>
    )
}

export default Button;