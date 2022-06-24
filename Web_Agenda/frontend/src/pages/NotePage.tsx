import React, { useState, useEffect } from "react";

interface Note {
    content: string;
    created: Date;
    updated: Date;
}

const NotePage = ({ match }: any) => {

    let noteID = match.params.id
    let [note, setNote] = useState()

    useEffect(() => {

    })

    let getNote = async () => {
        let response = await fetch('/api/notes/${noteID}/')
        let data = await response.json()
        setNote(data)
    }

    return (
        <div>
            <p>{note}</p>
        </div>
    )
}

export default NotePage