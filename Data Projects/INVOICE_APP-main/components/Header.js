export default function header({handlePrint}) {

    return(
        <>
            <header className="flex flex-col items-center
           justify-center mb-5 xl:flex-row xl:justify-between">
                <div>
                    <h1 className="front-bold uppercase tracking-wide text-4xl mb-3 ">Invoice</h1>
                </div>

                <div>
                    <ul className="flex flex col items-center justify-between flexwrap">
                        <li>
                            <button onClick={handlePrint}
                                    className="mt-5 bg-blue-500 text white font-bold
                    py-2 px-8 rounded shadow border-2 border-blue-5000 hover:bg-transparent
                    hover:text-blue-500 transition-all duration-300">
                                Print
                            </
                                button>
                        </li>

                        <li className="mx-2">
                            <button  className="mt-5 bg-red-500 text white font-bold
                    py-2 px-8 rounded shadow border-2 border-red-5000 hover:bg-transparent
                    hover:text-red-500 transition-all duration-300">Download</button>
                        </li>

                        <li>
                            <button  className="mt-5 bg-green-500 text white font-bold
                    py-2 px-8 rounded shadow border-2 border-green-5000 hover:bg-transparent
                    hover:text-green-500 transition-all duration-300">Send</button>
                        </li>
                    </ul>
                </div>
            </header>
        </>
    )
}