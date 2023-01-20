export default function clientDetails ({clientname,clientaddress}) {
    return(
        <>
            <section className="mt-5">

                <h2 className="text-xl uppercase">{clientname}</h2>
                <p>{clientaddress}</p>

            </section>
        </>
    )
}