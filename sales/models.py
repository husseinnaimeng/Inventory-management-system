from django.db import models

class OrderItem(models.Model):
    
    product  = models.ForeignKey('inventory.Product',on_delete=models.SET_NULL,null=True)
    customer = models.ForeignKey('customer.Customer',on_delete=models.SET_NULL,null=True,related_name='customer_order_item',blank=True)
    quantity = models.PositiveIntegerField(default=1,max_length=6)
    price    = models.DecimalField(max_digits=10,decimal_places=3,blank=True,null=True)
    def total(self):
        if self.price is not None:
            return self.price * self.quantity
        return self.product.sale_price * self.quantity

    def save(self,*args,**kwargs):
        self.cutomer = self.order.customer


"""
Order Statuses

    Pending: The order has been created but not yet processed. This is the initial status after an order is placed.
    
    Processing: The order is currently being processed. This means it is being prepared, items are being picked from the inventory, and it is getting ready for shipment.
    
    On Hold: The order is temporarily paused. This could be due to various reasons such as awaiting customer confirmation, payment issues, or stock verification.
    
    Completed: The order has been fully processed, shipped, and delivered to the customer.
    
    Cancelled: The order has been cancelled either by the customer or by the system due to some issue such as payment failure or stock unavailability.
    
    Refunded: The order has been refunded after a return or cancellation, and the customer has been reimbursed.
    
    Shipped: The order has been dispatched from the warehouse and is on its way to the customer.
    
    Delivered: The order has been delivered to the customer.
    
    Returned: The customer has returned the order after delivery, and it is being processed for return.
    
    Failed: The order could not be processed due to some issue, such as payment failure or inventory issues.

"""

class Order(models.Model):
    
    PENDING = 'Pending'
    PROCESSING = 'Processing'
    ON_HOLD = 'On Hold'
    COMPLETED = 'Completed'
    CANCELLED = 'Cancelled'
    REFUNDED = 'Refunded'
    SHIPPED = 'Shipped'
    DELIVERED = 'Delivered'
    RETURNED = 'Returned'
    FAILED = 'Failed'

    ORDER_STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (PROCESSING, 'Processing'),
        (ON_HOLD, 'On Hold'),
        (COMPLETED, 'Completed'),
        (CANCELLED, 'Cancelled'),
        (REFUNDED, 'Refunded'),
        (SHIPPED, 'Shipped'),
        (DELIVERED, 'Delivered'),
        (RETURNED, 'Returned'),
        (FAILED, 'Failed'),
    ]

    status = models.CharField(
        max_length=20,
        choices=ORDER_STATUS_CHOICES,
        default=PENDING,
    )
    cutomer     = models.ForeignKey('customer.Customer',on_delete=models.SET_NULL,null=True,blank=True)
    order_items = models.ManyToManyField(OrderItem,related_name='order')
    tax         = models.DecimalField(max_digits=10,decimal_places=3,default=0.000)

    def total(self):
        
        total = sum([order_item.total() for order_item in self.order_items.all() ])
        
        return total + self.tax
