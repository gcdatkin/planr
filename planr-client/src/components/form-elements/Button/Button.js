import FormElementLabel from "../FormElementLabel";

function Button(props) {

    return (
        <div className="">
            <button className="Button border border-gray-200 p-2 px-4 border border-blue-200 rounded bg-gray-100 hover:bg-gray-200 active:bg-gray-300 transition-colors duration-75">{props.value || "Button"}</button>
        </div>
    )
}

export default Button;