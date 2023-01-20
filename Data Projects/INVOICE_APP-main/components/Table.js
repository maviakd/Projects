export default function table ({amount}) {
    return(
        <>
            <table width="100%">
                <thead>
                <tr className="bg-gray-100 p-1">
                    <td>Item Description</td>
                    <td>Quantity</td>
                    <td>Price</td>
                    <td>Amount</td>
                    </tr>
                </thead>


                <tbody>
                <tr>
                    <td>Long Description</td>
                    <td>20</td>
                    <td>500</td>
                    <td>{amount}</td>
                </tr>
                </tbody>

            </table>
        </>
    )
}