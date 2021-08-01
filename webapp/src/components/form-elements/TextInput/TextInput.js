import FormElementLabel from "../FormElementLabel";

function TextInput(props) {

    return (
        <div className="">
            {props.label ? <FormElementLabel value={props.label} /> : ''}
            <input type="text" className="TextInput rounded border border-gray-300 bg-gray-50 p-2 w-full outline-none focus:bg-gray-50 transition-colors duration-75 mb-2"></input>
        </div>
    )
}

export default TextInput;