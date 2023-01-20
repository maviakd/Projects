export default function Footer ({name,address,email,website,phone,accountnumber,bankname}){
    return(
        <>
            <footer className="footer border-t-2 border-gray-300- pt-5">
                <ul className="flex flex-wrap item-center justify-center">
                    <li><span className="font-bold">Name:</span>{name}</li>
                    <li><span className="font-bold">Address:</span>{address}</li>
                    <li><span className="font-bold">Email:</span>{email}</li>
                    <li><span className="font-bold">Phone Number:</span>{phone}</li>
                    <li><span className="font-bold">Bank:</span>{bankname}</li>
                    <li><span className="font-bold">Account Number:</span>{accountnumber}</li>
                    <li><span className="font-bold">Account Holder:</span>{name}</li>

                    <li><span className="font-bold">Website:</span>{""}
                        <a
                            href={website} target="blank" rel="noopener noreferrer"> {website}
                        </a>
                        </li>
                </ul>
            </footer>
        </>
    )
}