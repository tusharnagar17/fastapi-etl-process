import React from "react"

export default function page({ searchParams }) {
    const { about } = searchParams
    return (
        <div>
            {/* About section */}
            <div className="">
                <span className="text-violet-600 font-semibold">
                    Table View
                </span>
                /<span> {about}</span>
            </div>

            {/* Table View */}
        </div>
    )
}
