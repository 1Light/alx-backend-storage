-- Assuming the table name is `metal_bands` and the columns are `band_name`, `style`, `formed`, `split`

-- Compute lifespan as (2022 - formed) and select bands with 'Glam rock' as their main style
SELECT
    band_name,
    (2022 - formed) AS lifespan
FROM
    metal_bands
WHERE
    style = 'Glam rock'
    AND split IS NOT NULL -- Ensure that the band has a split date if applicable
ORDER BY
    lifespan DESC;

