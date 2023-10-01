import * as sqlite from 'sqlite';
import xlsx  from 'xlsx';
import sqlite3  from 'sqlite3'

const workbook = xlsx.readFile('complete_data.xlsx');
const sheetName = workbook.SheetNames[0]; // Assuming data is in the first sheet
const worksheet = workbook.Sheets[sheetName];
const excelData = xlsx.utils.sheet_to_json(worksheet);

const db = await sqlite.open({
    filename: './capstonedb.db',
    driver: sqlite3.Database
});

// const db = new sqlite3.Database('capstonedb.db');

const createTableQuery = `
CREATE TABLE IF NOT EXISTS dataset (
    id integer primary key AUTOINCREMENT,
    Borehole_ID TEXT,
    Depth_From real,
    Depth_To real,
    Run_Length  real,
    True_Thickness real,
    Weathering real,
    Hardness real,
    Geotech_Domain TEXT,
    Jn_Description TEXT,
    Jr_Description TEXT,
    Ja_Description TEXT,
    Jw_Description TEXT,
    ESR_Conditions TEXT,
    Depth_underground real,
    RQD_m real,
    RQD_p real,
    Jn real,
    Jr real,
    Ja real,
    Jw real,
    Density real,
    Virgin_Stress real,
    UCS_Mpa real,
    UCS_Virgin_stress_ratio real,
    SRF real,
    Q_Value real,
    LNQ real,
    RMR real,
    ESR_VALUE real,
    Maximum_unsupported_span real
)
`;

// db.serialize(() => {
//     db.run(createTableQuery);
  
//     // Step 5: Import data into SQLite database
//     const insertQuery = `INSERT INTO dataset (
//       Borehole_ID,
//       Depth_From,
//       Depth_To,
//       Run_Length ,
//       True_Thickness,
//       Weathering,
//       Hardness,
//       Geotech_Domain,
//       Jn_Description,
//       Jr_Description,
//       Ja_Description,
//       Jw_Description,
//       ESR_Conditions,
//       Depth_underground,
//       RQD_m,
//       RQD_p,
//       Jn,
//       Jr,
//       Ja,
//       Jw,
//       Density,
//       Virgin_Stress,
//       UCS_Mpa,
//       UCS_Virgin_stress_ratio,
//       SRF,
//       Q_Value,
//       LNQ,
//       RMR,
//       ESR_VALUE,
//       Maximum_unsupported_span
//   ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`;
    
//     excelData.forEach(row => {
//       const values = Object.values(row);
//       db.run(insertQuery, values, err => {
//         if (err) {
//           console.error('Error inserting data:', err);
//         }
//       });
//     });
//   });

  
  // Close the database connection after all operations
  // db.close((err) => {
  //   if (err) {
  //     console.error('Error closing the database:', err.message);
  //   } else {
  //     console.log('Data imported successfully.');
  //   }
  // });

  // export async function check_delay(Delay, laborers, cash_flow, Errors, communication, Change_schedule, bid_price, scope_change, Weather_conditions, Accidents) {
  //   await db.run(`insert into price_plan (Delay, laborers, cash_flow, Errors, communication, Change_schedule, bid_price, scope_change, Weather_conditions, Accidents) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)`, [Delay, laborers, cash_flow, Errors, communication, Change_schedule, bid_price, scope_change, Weather_conditions, Accidents]);
  //   // const insertQuery = `INSERT INTO delays (Delay, laborers, cash_flow, Errors, communication, Change_schedule, bid_price, scope_change, Weather_conditions, Accidents) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);`;
  // }

//view all historical data
export async function GetHistory() {
const result = await db.all(`SELECT
                                Jn, Ja, Jr, Jw, UCS_Virgin_stress_ratio, RQD_p, Q_Value, SRF, RMR, ESR_VALUE, Maximum_unsupported_span
                                FROM dataset LIMIT 5 OFFSET 8`);
    return result
}

const result = await GetHistory()
console.log(result)

// UCS/Virgin stress
export async function GetUCS_virginStress() {
    const result = await db.all(`
        SELECT
            *
        FROM UCS_virginStress 
        ORDER BY id DESC
        LIMIT 5`);
        return result
    }
    
const resultUCS = await GetUCS_virginStress();
console.log("UCS Values")
console.log(resultUCS)


export async function predictUCS(Density, Depth, UCS, UCS_PreictedValue){
    //sql statement type - insert
    await db.run(`insert into UCS_virginStress (Density, Depth, UCS, UCS_PreictedValue) values (?, ?, ?, ?)`, [Density, Depth, UCS, UCS_PreictedValue]);

}





export async function GetSRF() {
    const result = await db.all(`
        SELECT * 
        FROM SRF
        INNER JOIN UCS_virginStress
            ON SRF.UCS_Id = UCS_virginStress.Id
        ORDER BY id DESC
        LIMIT 5`);
        return result
    }
    
const resultSRF = await GetSRF()
console.log("Before SRF")
console.log(resultSRF)

// RQD
// export async function GetRQD() {
//     const result = await db.all(`
//         SELECT
//         Depth_From,
//         Depth_To,
//         True_Thickness,
//         Hardness
//         FROM RQD 
//         ORDER BY id DESC
//         LIMIT 5`);
//         return result
//     }
    
// const resultRQD = await GetRQD()
// console.log(resultRQD)


// Q_Value
// export async function GetQ_Value() {
//     const result = await db.all(`
//         SELECT
//         Jn,
//         Jr,
//         Ja,
//         Jw,
//         SRF,
//         RDQ_p
//         FROM Q_Value 
//         ORDER BY id DESC
//         LIMIT 5`);
//         return result
//     }
    
// const resultQ_Value = await GetQ_Value()
// console.log(resultQ_Value)