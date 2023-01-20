export default function dates ({invoicenumber,invoicedate,duedate,amount}) {
    return(
        <>
            <section>
                <article className="my-5 flex items-end justify-end">
                    <ul>
                        <li className="p-1 "><span className="font-bold">Invoice #:</span>{invoicenumber}</li>
                        <li className="p-1 bg-gray-100"><span className="font-bold">Invoice Date:</span>{invoicedate}</li>
                        <li className="p-1"><span className="font-bold">Due Date:</span>{duedate}</li>
                        <li className="p-1"><span className="font-bold">Invoice Amount:</span>{amount}</li>
                    </ul>
                </article>
            </section>
        </>
    )
}