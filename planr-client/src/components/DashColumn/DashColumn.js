
function DashColumn(props) {

    return (
        <div className="DashColumn flex items-stretch flex-col flex-grow mx-2 box-border md:min-w-min min-w-full">
            <span className="font-semibold text-lg text-gray-500 mb-2 px-1">{props.title || ' '}</span>
            {props.children}
        </div>
    )
}

export default DashColumn;