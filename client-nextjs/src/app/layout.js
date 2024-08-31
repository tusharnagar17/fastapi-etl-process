import "./globals.css"

export const metadata = {
    title: "FastApi-Datapipeline",
    description: "fastApi-datapipeline",
}

export default function RootLayout({ children }) {
    return (
        <html lang="en">
            <body>{children}</body>
        </html>
    )
}
