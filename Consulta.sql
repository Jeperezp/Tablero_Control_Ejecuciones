SELECT 
    soh.SalesOrderID,
    soh.OrderDate,
    soh.CustomerID,
    soh.TotalDue,
    sod.ProductID,
    sod.OrderQty,
    sod.UnitPrice
FROM 
    Sales.SalesOrderHeader AS soh
    INNER JOIN Sales.SalesOrderDetail AS sod
        ON soh.SalesOrderID = sod.SalesOrderID
WHERE 
    soh.OrderDate > CAST('_Fecha_' AS date)
    AND soh.CustomerID = _codigo_cliente_
    AND sod.ProductID = _codigo_producto_
ORDER BY 
    soh.OrderDate;