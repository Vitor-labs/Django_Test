import React from "react";

interface Note {
    content: string;
    created: Date;
    updated: Date;
}

const ListItem = (note: Note) => {
    return (
        <div>
            <h1>{note.content}</h1>
        </div>
    )
}

export default ListItem