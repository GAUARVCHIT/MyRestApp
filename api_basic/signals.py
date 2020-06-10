from django.db.models.signals import post_save
# from django.contrib.auth.models import User
# from django.contrib.auth.models import Group
from .models import Customers,Results,PointsTableType,PointsTable


# def customer_profile(sender,  instance,update_fields , created, **kwargs,):

#     # if created:
#     #     if instance.position==1:
#     #         # instance.placement_point=20
#     #         # instance.placement_point.add(20)
            
#     #         print('gaurav '+str(instance.placement_point))


#         post_save.disconnect(customer_profile, sender=sender)
#         result=Results.objects.get(id=instance.id)
#         result.placement_point=20
#         result.save(update_fields=['placement_point'])
#         post_save.connect(customer_profile, sender=sender)

        
    
#     # if created:
#     #     group= Group.objects.get(name= 'customers')
#     #     instance.groups.add(group)

#     #     Customers.objects.create(
#     #         user=instance,
#     #         name=instance.username,
#     #     )

# post_save.connect(customer_profile,sender=Results)




# def generate_thumbnails(sender, instance=None, created=False, **kwargs):
# def customer_profile(sender,  update_fields ,  created=False,instance=None, **kwargs):

#     if not instance:
#         return

#     if hasattr(instance, '_dirty'):
#         return

#     result=Results.objects.get(id=instance.id)
#     result.placement_point=20
#     result.save(update_fields=['placement_point'])

#     try:
#         instance._dirty = True
#         instance.save()
#     finally:
#         del instance._dirty

# post_save.connect(customer_profile,sender=Results)



def save_favorite(sender, instance, **kwargs):
   fav = instance
   resultupdate=Results.objects.filter(id=fav.id)
   resultif=Results.objects.get(id=fav.id)
   position= resultif.position
   kills=resultif.kills

#    if resultif.points_table_type.id==1:
#     resultupdate.update(placement_point=4)
   
   for i in PointsTable.objects.all():
       if i.pointsTableType.id==resultif.points_table_type.id and i.rank==position :
           resultupdate.update(placement_point=i.placement_point,kill_points=i.kill_points*kills,Total_points=i.placement_point+i.kill_points*kills)
           break

    
   
   
post_save.connect(save_favorite, sender=Results)