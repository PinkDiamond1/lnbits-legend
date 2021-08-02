async def m001_initial(db):

    await db.execute(
        """
        CREATE TABLE IF NOT EXISTS Services (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            state TEXT NOT NULL,
            twitchuser TEXT NOT NULL,
            client_id TEXT NOT NULL,
            client_secret TEXT NOT NULL,
            wallet TEXT NOT NULL,
            onchain TEXT,
            servicename TEXT NOT NULL,
            authenticated BOOLEAN NOT NULL,
            token TEXT
        );
        """
    )

    await db.execute(
        """
        CREATE TABLE IF NOT EXISTS Donations (
            id TEXT PRIMARY KEY,
            wallet TEXT NOT NULL,
            name TEXT NOT NULL,
            message TEXT NOT NULL,
            cur_code TEXT NOT NULL,
            sats INT NOT NULL,
            amount FLOAT NOT NULL,
            service INTEGER NOT NULL,
            posted BOOLEAN NOT NULL,
            FOREIGN KEY(service) REFERENCES Services(id)
        );
        """
    )
