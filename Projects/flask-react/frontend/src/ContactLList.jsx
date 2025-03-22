import React from "react";

 const contactList = ({contacts}) => {

    if(!contacts){
        return <div>Loading...</div>;
    }
     return <div>
        <h1>Contacts</h1>
        <table>
            <thead>
                <tr>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Message</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {contacts.map((contact) => (
                    <tr key={contact.id}>
                        <td>{contact.Name}</td>
                        <td>{contact.Email}</td>
                        <td>{contact.Message}</td>
                        <td>
                            <button>Update</button>
                            <button>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
     </div>


 }

 export default contactList;
