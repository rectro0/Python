import React, { useState }  from "react";

const CotactForm = ({}) => {
    const [Name , setName] = useState("");
    const [Email , setEmail] = useState("");
    const [Message , setMessage] = useState("");

    const onSubmit = async(e) => {
        e.preventDefaut()

        const data= {
            Name,
            Email,
            Message,
        }
        const url="http://127.0.0.1:5000/create_contact"
        const options ={
            method: "POST",
            Headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)     
        }
        const response = await(url , options)

        if(response.status != 201 && response.status != 200){
            const data = await response.json()
            alert(data.message)
        }else{
            
        }
    };
    return (<Form onSubmit={onSubmit}>
        <div>
            <label htmlFor="Name"></label>
            <input type="text" id="Name" value={Name} onChange={(e) => setName(e.target.value)} />
            <label htmlFor="Email"></label>
            <input type="text"  id="Email" value={Email} onChange={(e) => setEmail(e.target.value)} />
            <label htmlFor="Message"></label>
            <input type="text" id="Message" value={Message} onChange={(e) => setMessage(e.target.value)} />
        </div>
        <button type="submit">Create Contact</button>
    </Form>
    );


};

export default CotactForm;