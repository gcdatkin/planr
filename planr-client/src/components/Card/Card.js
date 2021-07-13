
function Card(props) {

    return (
        <div className="Card bg-gray-100 rounded shadow p-4 mb-4 flex flex-col flex-wrap content-start items-stretch overflow-hidden min-w-0">
            <span className="font-semibold w-max block flex-grow mb-1">{props.title}</span>
            {props.children}
        </div>
    )
}

export default Card;