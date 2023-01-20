import './App.css';
import React, { useState,useRef, useEffect } from "react";
import Header from "./components/Header";
import MainDetails from "./components/MainDetails";
import Notes from "./components/Notes";
import ClientDetails from "./components/ClientDetails";
import Dates from "./components/Dates";
import Footer from "./components/Footer"
import Table from "./components/Table"


function App() {

    const handlePrint = () => {
        window.print()
    }
    const [showInvoice,setShowInvoice] = useState(false)

    const[name, setName] = useState("")
    const[address, setAddress] = useState("")
    const[email, setEmail] = useState("")
    const[phone, setPhone] = useState("")
    const[bankname, setBankName] = useState("")
    const[bankAccount, setBankaccount] = useState("")
    const[website, setWebsite] = useState("")
    const[clientname, setClientName] = useState("")
    const[clientaddress, setClientaddress] = useState("")
    const[invoicenumber, setInvoicenumber] = useState("")
    const[invoicedate, setInvoicedate] = useState("")
    const[duedate, setDuedate] = useState("")
    const[notes, setNotes] = useState("")
    const[amount, setAmount] = useState("")
    const [description, setDescription] = useState("")
    const [quantity, setQuantity] = useState("")
    const [price, setPrice] = useState("")
    const [list, setList] = useState([])
    const [total, setTotal] = useState(0)
    const [width] = useState(641)



    return (
        <>
            <main className="m-5 p-5 md:max-w-l md:mx-auto lg:max-w-2xl xl:max-w-4xl bg-white rounded shadow">
                {showInvoice ?
                    <div>
                    {/* Start Of The Header */}
                    <Header handlePrint={handlePrint} />
                    {/* End of Header */}

                    {/* Your Detail desription*/}

                    <MainDetails name={name} address={address}/>

                    {/* Your End of your Descriptions */}

                    {/*Client's Details */}

                    <ClientDetails clientname={clientname} clientaddress={clientaddress} />

                    {/* End of Client's details */}

                    {/* Dates */}

                    <Dates invoicenumber={invoicenumber} invoicedate={invoicedate} duedate={duedate} amount={amount}/>
                    {/* End of Dates */}

                    {/* Table */}

                    <Table amount={amount} description={description} price={price} quantity={quantity}/>
                    {/* End of Table */}

                    {/* Detailed Notes */}

                    <Notes notes={notes}/>

                    {/* End of Detailed Notes*/}

                    {/* Footer */}
                    <Footer name={name}
                            address={address}
                            website={website}
                            email={email}
                            bankname={bankname}
                            phone={phone}
                            accountnumber={bankAccount}
                    />
                    {/* End Footer */}

                        <button onClick={() => setShowInvoice(false)} className="mt-5 bg-blue-500 text white font-bold
                    py-2 px-8 rounded shadow border-2 border-blue-5000 hover:bg-transparent
                    hover:text-blue-500 transition-all duration-300"> Edit Information </button>

                </div>
                    : (
                        <>
                            {/* Name, address, email,phone number,bank,bank account number,website, client name, client
                            address, invoice number, date, due date, notes */}

                    <div className="flex flex-col
                    justify-center">

                        <label htmlFor="name">Enter your full name</label>
                    <input
                        type="text"
                        name="name"
                        id="name"
                        placeholder="Enter your name"
                        autoComplete="off"
                        value={name}
                        onChange={(e) => setName(e.target.value)}
                    />
                        <label htmlFor="address">Enter your Address</label>
                        <input
                            type="text"
                            name="address"
                            id="address"
                            placeholder="Enter your address"
                            autoComplete="off"
                            value={address}
                            onChange={(e) => setAddress(e.target.value)}
                        />

                        <label htmlFor="email">Enter your email</label>
                        <input
                            type="text"
                            name="email"
                            id="email"
                            placeholder="Enter your email"
                            autoComplete="off"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                        />

                        <label htmlFor="Phone">Enter your Phone #</label>
                        <input
                            type="text"
                            name="Phone"
                            id="Phone"
                            placeholder="Enter your Phone"
                            autoComplete="off"
                            value={phone}
                            onChange={(e) => setPhone(e.target.value)}
                        />

                        <label htmlFor="Bank">Enter your Bank name</label>
                        <input
                            type="text"
                            name="Bank"
                            id="Bank"
                            placeholder="Enter your Bank"
                            autoComplete="off"
                            value={bankname}
                            onChange={(e) => setBankName(e.target.value)}
                        />

                        <label htmlFor="BankAccount">Enter your Bank Account</label>
                        <input
                            type="text"
                            name="BankAccount"
                            id="BankAccount"
                            placeholder="Enter your BankAccount"
                            autoComplete="off"
                            value={bankAccount}
                            onChange={(e) => setBankaccount(e.target.value)}
                        />

                        <label htmlFor="Website">Enter your Website</label>
                        <input
                            type="url"
                            name="website"
                            id="website"
                            placeholder="Enter your website"
                            autoComplete="off"
                            value={website}
                            onChange={(e) => setWebsite(e.target.value)}
                        />

                        <label htmlFor="Client Name">Enter your Clients Name</label>
                        <input
                            type="text"
                            name="Client Name"
                            id="Client Name"
                            placeholder="Enter your Client Name"
                            autoComplete="off"
                            value={clientname}
                            onChange={(e) => setClientName(e.target.value)}
                        />

                        <label htmlFor="client Address">Enter your Client address</label>
                        <input
                            type="text"
                            name="client Address"
                            id="client Address"
                            placeholder="Enter your client Address"
                            autoComplete="off"
                            value={clientaddress}
                            onChange={(e) => setClientaddress(e.target.value)}
                        />

                        <label htmlFor="Amount">Enter The Invoice Amount</label>
                        <input
                            type="text"
                            name="Amount"
                            id="Amount"
                            placeholder="Enter your Amount"
                            autoComplete="off"
                            value={amount}
                            onChange={(e) => setAmount(e.target.value)}
                        />

                        <label htmlFor="InvoiceNumber">Enter your Invoice Number</label>
                        <input
                            type="date"
                            name="InvoiceNumber"
                            id="InvoiceNumber"
                            placeholder="Enter your InvoiceNumber"
                            autoComplete="off"
                            value={invoicenumber}
                            onChange={(e) => setInvoicenumber(e.target.value)}
                        />

                        <label htmlFor="Invoice Date ">Enter your Invoice Date</label>
                        <input
                            type="date"
                            name="Invoice Date"
                            id="Invoice Date"
                            placeholder="Enter your Invoice Date"
                            autoComplete="off"
                            value={invoicedate}
                            onChange={(e) => setInvoicedate(e.target.value)}
                        />

                        <label htmlFor="Due Date">Enter your DueDate</label>
                        <input
                            type="date"
                            name="Due Date"
                            id="Due Date"
                            placeholder="Enter your Due Date"
                            autoComplete="off"
                            value={duedate}
                            onChange={(e) => setDuedate(e.target.value)}
                        />

                        <label htmlFor="Note">Additional Notes</label>
                        <input
                            type="text"
                            name="Note"
                            id="Note"
                            placeholder="Enter your Note"
                            autoComplete="off"
                            value={notes}
                            onChange={(e) => setNotes(e.target.value)}
                        />

                    <button onClick={() => setShowInvoice(true)} className="bg-blue-500 text white font-bold
                    py-2 px-8 rounded shadow border-2 border-blue-5000 hover:bg-transparent
                    hover:text-blue-500 transition-all duration-300">
                    Preview Invoice
                    </button>
                    </div>
                         </>
                    )}
                    </main>
                    </>
    )}

export default App;
