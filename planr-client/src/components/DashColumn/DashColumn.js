
function DashColumn(props) {

    return (
        <div className="DashColumn flex items-stretch flex-col justify-between flex-grow mx-2 box-border md:min-w-min min-w-full">
            {props.children}
        </div>
    )
}

export default DashColumn;