import { useState, useEffect } from "react";

import ListItem from "../components/ListItem";
import AddButton from "../components/AddButton";

interface Note {
    id: number
    content: string
    created: Date
    updated: Date
}

const NotesListPage = () => {

    let [notes, setNotes] = useState([])

    useEffect(() => {
        getNotes()
    }, [])

    let getNotes = async () => {
        let response = await fetch("http://localhost:8000/api/notes/")
        let data = await response.json()
        setNotes(data)
    }

    return (
        <div className="notes">
            <div className="notes-header">
                <h2 className="notes-title">
                    &#9782; Notes:
                </h2>
                <p className="notes-count">
                    {notes.length}
                </p>
            </div>
            <div className="notes-list">
                {notes.map((note, id) => (
                    <ListItem key={id} note={note} />
                ))}
            </div>
            <AddButton />
        </div>
    )
}

export default NotesListPage