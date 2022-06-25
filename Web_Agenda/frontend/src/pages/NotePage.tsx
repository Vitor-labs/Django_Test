import { useState, useEffect } from "react";
import { Link, useParams, useNavigate } from "react-router-dom";

import CheckButton from "../components/CheckButton";
import RemoveButton from "../components/RemoveButton";

const NotePage = (_id: any) => {
    let match = useParams()
    let [note, setNote] = useState<any | null>(null)

    let note_id = match["id"];

    useEffect(() => {
        getNote()

    }, [note_id])

    // CRUD Create
    let createNote = async () => {
        await fetch(`http://localhost:8000/api/note/add/`, {
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(note)
        })
    }

    // CRUD Read
    let getNote = async () => {
        if (note_id === 'add') return

        let response = await fetch(`http://localhost:8000/api/note/${note_id}/`)
        let data = await response.json()
        setNote(data)
    }

    // CRUD Update
    let updateNote = async () => {
        let response = await fetch(`http://localhost:8000/api/note/${note_id}/update/`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                content: note.content
            })
        })
        let data = await response.json()
        setNote(data)
    }

    // CRUD Delete
    let deleteNote = async () => {
        await fetch(`http://localhost:8000/api/note/${note_id}/delete/`, {
            method: "DELETE",
            headers: {
                "Content-Type": "application/json"
            }
        })
        let navigate = useNavigate()
        navigate("http://localhost:3000/")
    }
    // =====================================================================

    let handleChangeOnNote = () => {
        console.log('NOTE:', note)
        if (note_id !== 'add' && note.content == '') {
            deleteNote()
        } else if (note_id !== 'add') {
            updateNote()
        } else if (note_id === 'add' && note.content !== null) {
            createNote()
        }
        let navigate = useNavigate()
        navigate("http://localhost:3000/")
    }

    return (
        <div className="note">
            <div className="note-header">
                <h3>
                    <Link to={"/"} onClick={handleChangeOnNote}>
                        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 32 32">
                            <title>chevron-left-circle</title>
                            <path d="M16 32c-8.822 0-16-7.178-16-16s7.178-16 16-16c8.822 0 16 7.178 16 16s-7.178 16-16 16zM16 2c-7.72 0-14 6.28-14 14s6.28 14 14 14c7.72 0 14-6.28 14-14s-6.28-14-14-14z"></path>
                            <path d="M13 16l7-7v-3l-10 10 10 10v-3l-7-7z"></path>
                        </svg>
                    </Link>
                </h3>
                {note_id !== 'add' ? (
                    <Link to="/" className="floating-button" onClick={deleteNote}>
                        <RemoveButton />
                    </Link>
                ) : (
                    <Link to="/" className="floating-button" onClick={createNote}>
                        <CheckButton />
                    </Link>
                )}

            </div>
            <textarea onChange={(e) => { setNote({ ...note, 'content': e.target.value }); console.log(e) }} defaultValue={note?.content}></textarea>
        </div >
    )
}

export default NotePage