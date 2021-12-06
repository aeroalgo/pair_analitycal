code = """<?xml version="1.0" encoding="utf-16"?>
<GraphDataBase xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:type="GraphViewData">
  <EditData VersionString="2.3" TemplateClass="Script">
    <ViewModel>
      <Model Scale="0.53032135064529418">
        <Block Key="Источник1" Category="TradableSecurity" Location="141 144.81881225706948" TypeName="TradableSecuritySourceItem">
          <EditItem Guid="13E828E4-4633-455C-B81B-730B003D8002" CodeName="var0" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" />
        </Block>
        <Block Key="Закрытие1" Category="TradeMath" Location="165 228.81881225706948" TypeName="ConverterItem">
          <EditItem Guid="566F73F2-A440-48DF-A5F7-5BA11ABF3973" CodeName="Закрытие1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Close, TSLab.Script.Handlers, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Pane Key="Главная" Category="GraphPane" Location="1 229.81881225706948" Order="0" IsVisible="true" HideLegend="false" LeftAxisPrecision="-1" LeftAxisByPercents="false" LeftDownHysteresis="0" LeftUpHysteresis="0" RightAxisPrecision="-1" RightAxisByPercents="false" RightDownHysteresis="0" RightUpHysteresis="0" />
        <Block Key="Источник2" Category="TradableSecurity" Location="341 144.81881225706948" TypeName="TradableSecuritySourceItem">
          <EditItem Guid="dae2c52a-3337-4eea-9caf-f302f70848d5" CodeName="Источник2" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" />
        </Block>
        <Block Key="Закрытие2" Category="TradeMath" Location="380.99999999999994 227.81881225706948" TypeName="ConverterItem">
          <EditItem Guid="fb660a86-4a24-4129-9ebe-d6ecb75f223f" CodeName="Закрытие2" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Close, TSLab.Script.Handlers, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Pane Key="Главная1" Category="GraphPane" Location="0 337.81881225706945" Order="1" IsVisible="true" HideLegend="false" LeftAxisPrecision="-1" LeftAxisByPercents="false" LeftDownHysteresis="0" LeftUpHysteresis="0" RightAxisPrecision="-1" RightAxisByPercents="false" RightDownHysteresis="0" RightUpHysteresis="0" />
        <Pane Key="Главная2" Category="GraphPane" Location="601 147.81881225706948" Order="2" IsVisible="true" HideLegend="false" LeftAxisPrecision="-1" LeftAxisByPercents="false" LeftDownHysteresis="0" LeftUpHysteresis="0" RightAxisPrecision="10" RightAxisByPercents="false" RightDownHysteresis="0" RightUpHysteresis="0" />
        <Block Key="НачальныйBuy1" Category="Const" Location="473.99999999999994 338.81881225706945" TypeName="ConverterItem">
          <EditItem Guid="4a074d54-81cb-4469-bbd7-698000095100" CodeName="НачальныйBuy1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.ConstGen, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="Вычесть" Category="TradeMath" Location="606.28473713484857 494.81881225706945" TypeName="TwoOrMoreInputsItem">
          <EditItem Guid="2f738f30-d395-4d0e-b317-1ef8da486fa4" CodeName="Вычесть" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Sub, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="ОтноситКомисси" Category="TradeMath" Location="796 135.81881225706948" TypeName="ConverterItem">
          <EditItem Guid="e6b68b96-6c04-4a35-ae99-d4754ce84a7c" CodeName="ОтноситКомисси" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.RelativeCommission, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="CommissionPct" TypeName="Double" Value="0.08" />
              <Parameter Name="MarginPct" TypeName="Double" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ОтноситКомисси1" Category="TradeMath" Location="790 200.81881225706948" TypeName="ConverterItem">
          <EditItem Guid="fafbe06d-5eaa-4e2a-8083-1c44684e3909" CodeName="ОтноситКомисси1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.RelativeCommission, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="CommissionPct" TypeName="Double" Value="0.08" />
              <Parameter Name="MarginPct" TypeName="Double" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ТекущийBid" Category="TradeMath" Location="1086 207.81881225706948" TypeName="ConverterItem">
          <EditItem Guid="b9b703a9-062d-4a17-bef8-3eeef736f4bd" CodeName="ТекущийBid" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Bid, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="ТекущийAsk" Category="TradeMath" Location="1084 150.81881225706948" TypeName="ConverterItem">
          <EditItem Guid="d4eb7727-f03d-427e-bfc8-98bbb9fe46d6" CodeName="ТекущийAsk" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Ask, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="ТекущийAsk1" Category="TradeMath" Location="1251 158.81881225706948" TypeName="ConverterItem">
          <EditItem Guid="59880fc9-a9e3-4bb7-93ef-e33775073ab5" CodeName="ТекущийAsk1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Ask, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="ТекущийBid1" Category="TradeMath" Location="1253 215.81881225706948" TypeName="ConverterItem">
          <EditItem Guid="528ff5a6-41dd-4861-8ebb-e6101592aeaf" CodeName="ТекущийBid1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Bid, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="УмножитНа" Category="TradeMath" Location="735 49.818812257069482" TypeName="ConverterItem">
          <EditItem Guid="547706d7-5a1c-4ec9-be62-997509b5f568" CodeName="УмножитНа" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Multiply, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Coef" TypeName="Double" Value="0.5" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="Вес2" Category="Const" Location="359 75.818812257069482" TypeName="ConverterItem">
          <EditItem Guid="b55db2ba-af03-4132-b68e-fb47ff5f0d31" CodeName="Вес2" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.ConstGen, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Value" TypeName="Double" Value="1000" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="Формула5" Category="Formula" Location="318.71526286515143 417.93316311474621" TypeName="DoubleCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="143" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="82a66f29-73ee-47d6-a4ea-69150597b557" CodeName="Формула5" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.DoubleCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="ТекущийAsk==0||ТекущийBid==0||ТекущийAsk1==0||ТекущийBid1==0?Закрытие1/Закрытие2*Вес2:ТекущийAsk/ТекущийBid1*Вес2" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="Формула6" Category="Formula" Location="1093.3711053732227 374.07660151062441" TypeName="DoubleCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="143" ResizablePartHeight="80" OpenParams="true">
          <EditItem Guid="ca52e6d2-1a57-48fc-9175-ff3de1836b6c" CodeName="Формула6" IsParametersVisible="true" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.DoubleCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="ТекущийAsk==0||ТекущийBid==0||ТекущийAsk1==0||ТекущийBid1==0?Закрытие1/Закрытие2*Вес2:ТекущийBid/ТекущийAsk1*Вес2" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="Формула7" Category="Formula" Location="331.16054720448483 493.79874385650885" TypeName="DoubleCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="143" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="5438d90b-29d1-493b-87f7-d4f7eb6607a7" CodeName="Формула7" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.DoubleCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="ТекущийAsk==0||ТекущийBid==0||ТекущийAsk1==0||ТекущийBid1==0?(Закрытие1/Закрытие2*Вес2)*-НачальныйBuy1:(ТекущийBid/ТекущийAsk1*Вес2)*-НачальныйBuy1" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="Формула8" Category="Formula" Location="1096 455.81881225706945" TypeName="DoubleCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="143" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="e8e645da-c2b2-4209-ab7f-ffc7912bc416" CodeName="Формула8" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.DoubleCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="ТекущийAsk==0||ТекущийBid==0||ТекущийAsk1==0||ТекущийBid1==0?(Закрытие1/Закрытие2*Вес2)*НачальныйSell1:(ТекущийAsk/ТекущийBid1*Вес2)*НачальныйSell1" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="Вычесть1" Category="TradeMath" Location="1353 461.81881225706945" TypeName="TwoOrMoreInputsItem">
          <EditItem Guid="5c043480-d68a-446e-9d5a-966d7c9be954" CodeName="Вычесть1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Sub, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="НачальныйSell1" Category="Const" Location="1112 297.81881225706945" TypeName="ConverterItem">
          <EditItem Guid="c149f466-7e54-4b9f-b86a-ca97cdda67be" CodeName="НачальныйSell1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.ConstGen, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="Объем1" Category="TradeMath" Location="165 432.81881225706945" TypeName="ConverterItem">
          <EditItem Guid="5329e716-896f-413e-9a82-4da473241862" CodeName="Объем1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Volume, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="Объем" Category="TradeMath" Location="157 368.81881225706945" TypeName="ConverterItem">
          <EditItem Guid="d0780ed2-4afb-490d-b5ea-6ea119127980" CodeName="Объем" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Volume, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="Формула3" Category="Formula" Location="919 45.818812257069482" TypeName="DoubleCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="143" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="ef90887b-3224-4562-806e-2a85b5001919" CodeName="Формула3" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.DoubleCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="Math.Round((УмножитНа/Закрытие1)/ШагЛота)*ШагЛота" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="Формула4" Category="Formula" Location="1176 44.818812257069482" TypeName="DoubleCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="143" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="de793c33-7401-413c-a2fd-c2808cb33eb9" CodeName="Формула4" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.DoubleCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="Math.Round((УмножитНа/Закрытие2)/ШагЛота1)*ШагЛота1" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ШагЛота" Category="TradeMath" Location="1412 49.818812257069482" TypeName="ConverterItem">
          <EditItem Guid="c1ee2d69-996b-45a8-b9b5-b4505c9f3789" CodeName="ШагЛота" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.LotTick, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="ШагЛота1" Category="TradeMath" Location="1412 103.81881225706948" TypeName="ConverterItem">
          <EditItem Guid="b04674db-7725-4d72-90fd-395f0ffe913e" CodeName="ШагЛота1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.LotTick, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="ОчереЗаявоЦена1" Category="TradeMath" Location="323.58345013037263 0" TypeName="ConverterItem">
          <EditItem Guid="04218c9a-79a3-48b6-a169-9101f69d6dee" CodeName="ОчереЗаявоЦена1" IsParametersVisible="false" OnlyValueHandlersCanUsed="true" HandlerTypeName="TSLab.Script.Handlers.OrderBookPrice, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Buy" TypeName="Boolean" Value="false" />
              <Parameter Name="Index" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ОчереЗаявоЦена" Category="TradeMath" Location="162.24531566860691 60.501800423162138" TypeName="ConverterItem">
          <EditItem Guid="906625ce-3b51-45c9-962a-3e142b2170e9" CodeName="ОчереЗаявоЦена" IsParametersVisible="false" OnlyValueHandlersCanUsed="true" HandlerTypeName="TSLab.Script.Handlers.OrderBookPrice, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Buy" TypeName="Boolean" Value="false" />
              <Parameter Name="Index" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="Вычесть2" Category="TradeMath" Location="1357.9315381340484 611.89779906998" TypeName="TwoOrMoreInputsItem">
          <EditItem Guid="e71ae0c4-075a-4a88-a943-95afe94c26f1" CodeName="Вычесть2" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Sub, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="Вычесть3" Category="TradeMath" Location="767.18963180996934 582.38377976098866" TypeName="TwoOrMoreInputsItem">
          <EditItem Guid="6964a99f-bf08-46ff-8dc8-8373b33df3e8" CodeName="Вычесть3" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Sub, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="Формула9" Category="Formula" Location="348.07914421096075 575.98067254953742" TypeName="DoubleCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="143" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="0be1d891-29b2-4c58-97db-efd97e8ca3f5" CodeName="Формула9" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.DoubleCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="ТекущийAsk==0||ТекущийBid==0||ТекущийAsk1==0||ТекущийBid1==0?Закрытие1/Закрытие2*Вес2:ТекущийBid/ТекущийAsk1*Вес2" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="Формула10" Category="Formula" Location="1094.539276984136 543.48422474532742" TypeName="DoubleCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="143" ResizablePartHeight="80" OpenParams="true">
          <EditItem Guid="c82dcac1-a4fb-4390-81ac-0b25ebbda8c1" CodeName="Формула10" IsParametersVisible="true" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.DoubleCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="ТекущийAsk==0||ТекущийBid==0||ТекущийAsk1==0||ТекущийBid1==0?Закрытие1/Закрытие2*Вес2:ТекущийAsk/ТекущийBid1*Вес2" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="СвязаннПарамет1" Category="Usual" Location="1523.565793608087 576.06211728087624" TypeName="ParameterShareItem">
          <EditItem ParameterName1="MaPeriod" ParameterName2="MaPeriod" />
        </Block>
        <Block Key="ЗакрПозиПоРынк3" Category="ClosePosition" Location="1460.9632214431952 763.63627258668419" TypeName="ClosePositionByMarketItem">
          <EditItem Guid="9bd78a71-ba44-4932-8856-12f3063f2732" CodeName="ЗакрПозиПоРынк3" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="AddOpenName" TypeName="Boolean" Value="false" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЗакрПозиПоРынк2" Category="ClosePosition" Location="1242.9632214431952 767.63627258668419" TypeName="ClosePositionByMarketItem">
          <EditItem Guid="0f4854f9-45c0-477a-a329-6b4705fa58e3" CodeName="ЗакрПозиПоРынк2" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="AddOpenName" TypeName="Boolean" Value="false" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЛогичесФормула3" Category="Formula" Location="1020.9632214431952 683.63627258668419" TypeName="BoolCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="190" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="65911a14-2b94-419e-83e3-c5f7665f1c02" CodeName="ЛогичесФормула3" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.BoolCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="Вычесть1&gt;Формула8&amp;&amp;ТекущийAsk!=0&amp;&amp;ТекущийBid!=0&amp;&amp;ТекущийAsk1!=0&amp;&amp;ТекущийBid1!=0" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЛогичесФормула2" Category="Formula" Location="1017.9632214431952 770.63627258668419" TypeName="BoolCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="190" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="1d9025aa-62c9-4fd0-be41-66e1403c232b" CodeName="ЛогичесФормула2" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.BoolCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="Вычесть2&lt;0&amp;&amp;ТекущийAsk!=0&amp;&amp;ТекущийBid!=0&amp;&amp;ТекущийAsk1!=0&amp;&amp;ТекущийBid1!=0" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЛогичесФормула1" Category="Formula" Location="317.96322144319515 775.63627258668419" TypeName="BoolCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="190" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="cac6e5a9-938a-4bc8-aba8-2e4a665d8982" CodeName="ЛогичесФормула1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.BoolCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="Вычесть3&gt;0&amp;&amp;ТекущийAsk!=0&amp;&amp;ТекущийBid!=0&amp;&amp;ТекущийAsk1!=0&amp;&amp;ТекущийBid1!=0" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЗакрПозиПоРынк1" Category="ClosePosition" Location="775.96322144319515 777.63627258668419" TypeName="ClosePositionByMarketItem">
          <EditItem Guid="877c706c-968a-4fc9-9546-d579ec11cd4d" CodeName="ЗакрПозиПоРынк1" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="AddOpenName" TypeName="Boolean" Value="false" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЗакрПозиПоРынк" Category="ClosePosition" Location="553.96322144319515 774.63627258668419" TypeName="ClosePositionByMarketItem">
          <EditItem Guid="706668b7-846a-488a-9330-eb675af89590" CodeName="ЗакрПозиПоРынк" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="AddOpenName" TypeName="Boolean" Value="false" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЛогичесФормула" Category="Formula" Location="301.81899800569511 691.18883571168419" TypeName="BoolCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="190" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="eb739eb0-4529-4a18-a082-e9eed5836cd9" CodeName="ЛогичесФормула" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.BoolCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="Вычесть&lt;Формула7&amp;&amp;ТекущийAsk!=0&amp;&amp;ТекущийBid!=0&amp;&amp;ТекущийAsk1!=0&amp;&amp;ТекущийBid1!=0" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ОткрПозиПоРынк14" Category="OpenPosition" Location="787.96322144319515 674.63627258668419" TypeName="OpenPositionByMarketItem">
          <EditItem Guid="6d38f498-b24b-4084-bc2f-022103d5c192" CodeName="ОткрПозиПоРынк14" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="Long" TypeName="Boolean" Value="false" />
              <Parameter Name="Shares" TypeName="Double" Value="0.4" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ОткрПозиПоРынк" Category="OpenPosition" Location="555.96322144319515 671.63627258668419" TypeName="OpenPositionByMarketItem">
          <EditItem Guid="e852f070-827f-4dc3-9c8c-7958cb0765b7" CodeName="ОткрПозиПоРынк" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="Long" TypeName="Boolean" Value="true" />
              <Parameter Name="Shares" TypeName="Double" Value="1" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ОткрПозиПоРынк16" Category="OpenPosition" Location="1257.2373539338571 659.13574324652586" TypeName="OpenPositionByMarketItem">
          <EditItem Guid="ac283a46-787c-4bbd-885c-d436fd6144f1" CodeName="ОткрПозиПоРынк16" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="Long" TypeName="Boolean" Value="false" />
              <Parameter Name="Shares" TypeName="Double" Value="0.001" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ОткрПозиПоРынк9" Category="OpenPosition" Location="1453.2373539338571 655.13574324652586" TypeName="OpenPositionByMarketItem">
          <EditItem Guid="146f7d1c-b753-4e91-ac3a-9899a47b8926" CodeName="ОткрПозиПоРынк9" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="Long" TypeName="Boolean" Value="true" />
              <Parameter Name="Shares" TypeName="Double" Value="0.4" />
            </Parameters>
          </EditItem>
        </Block>
        <Pane Key="Главная3" Category="GraphPane" Location="1524.0936737284076 225.81306295754337" Order="3" IsVisible="true" HideLegend="false" LeftAxisPrecision="-1" LeftAxisByPercents="false" LeftDownHysteresis="0" LeftUpHysteresis="0" RightAxisPrecision="10" RightAxisByPercents="false" RightDownHysteresis="0" RightUpHysteresis="0" />
        <Block Key="Вычесть4" Category="TradeMath" Location="667.58138500869336 1029.7663990520414" TypeName="TwoOrMoreInputsItem">
          <EditItem Guid="7f1940bd-11d6-45a6-a91e-cbe75fc72a6b" CodeName="Вычесть4" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Sub, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="Вычесть5" Category="TradeMath" Location="675.74869915563181 1166.3582442563647" TypeName="TwoOrMoreInputsItem">
          <EditItem Guid="34a6f4dd-c5fe-4651-bc9f-d968eaae3e07" CodeName="Вычесть5" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Sub, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="ОткрПозиПоРынк2" Category="OpenPosition" Location="552.84833797724446 1221.721857351874" TypeName="OpenPositionByMarketItem">
          <EditItem Guid="d61b6e97-a11b-455f-9d50-8d280afbac37" CodeName="ОткрПозиПоРынк2" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="Long" TypeName="Boolean" Value="true" />
              <Parameter Name="Shares" TypeName="Double" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ОткрПозиПоРынк18" Category="OpenPosition" Location="784.84833797724446 1224.721857351874" TypeName="OpenPositionByMarketItem">
          <EditItem Guid="f17dbdb3-765e-42b2-957a-921244c2fc2e" CodeName="ОткрПозиПоРынк18" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="Long" TypeName="Boolean" Value="false" />
              <Parameter Name="Shares" TypeName="Double" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЛогичесФормула9" Category="Formula" Location="298.70411453974441 1241.2744204768742" TypeName="BoolCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="190" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="ba8e52cc-2ce4-4320-9da6-f42003188974" CodeName="ЛогичесФормула9" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.BoolCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="Вычесть4&lt;Формула11&amp;&amp;ТекущийAsk!=0&amp;&amp;ТекущийBid!=0&amp;&amp;ТекущийAsk1!=0&amp;&amp;ТекущийBid1!=0" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЗакрПозиПоРынк10" Category="ClosePosition" Location="550.84833797724446 1324.721857351874" TypeName="ClosePositionByMarketItem">
          <EditItem Guid="b7ef287f-7565-4143-9d20-d465861bdc10" CodeName="ЗакрПозиПоРынк10" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="AddOpenName" TypeName="Boolean" Value="false" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЗакрПозиПоРынк11" Category="ClosePosition" Location="772.84833797724446 1327.721857351874" TypeName="ClosePositionByMarketItem">
          <EditItem Guid="37534877-5090-41e8-8b51-36f859a68f04" CodeName="ЗакрПозиПоРынк11" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="AddOpenName" TypeName="Boolean" Value="false" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЛогичесФормула10" Category="Formula" Location="314.84833797724446 1325.721857351874" TypeName="BoolCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="190" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="6955c8b6-1087-486d-8163-8ab0154fe3dc" CodeName="ЛогичесФормула10" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.BoolCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="Вычесть5&gt;0&amp;&amp;ТекущийAsk!=0&amp;&amp;ТекущийBid!=0&amp;&amp;ТекущийAsk1!=0&amp;&amp;ТекущийBid1!=0" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="Вычесть6" Category="TradeMath" Location="1440.4195168519823 1148.0479868889443" TypeName="TwoOrMoreInputsItem">
          <EditItem Guid="1beacfbc-52e9-432f-987d-56e5d7f508b9" CodeName="Вычесть6" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Sub, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="Вычесть7" Category="TradeMath" Location="1432.2522027050441 1011.456141684621" TypeName="TwoOrMoreInputsItem">
          <EditItem Guid="d4b51f61-8503-455c-9f80-68dfb92af09a" CodeName="Вычесть7" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.Sub, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="ЛогичесФормула4" Category="Formula" Location="1015.265457330984 1235.3880403598951" TypeName="BoolCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="190" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="d1ecd16e-3af4-444e-8a96-53e574f24c31" CodeName="ЛогичесФормула4" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.BoolCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="Вычесть7&gt;Формула12&amp;&amp;ТекущийAsk!=0&amp;&amp;ТекущийBid!=0&amp;&amp;ТекущийAsk1!=0&amp;&amp;ТекущийBid1!=0" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЛогичесФормула5" Category="Formula" Location="1030.0848417259385 1318.4281771610163" TypeName="BoolCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="190" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="6e26ecee-0dbf-4b9d-bdf1-2a35b353c463" CodeName="ЛогичесФормула5" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.BoolCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="Вычесть6&lt;0&amp;&amp;ТекущийAsk!=0&amp;&amp;ТекущийBid!=0&amp;&amp;ТекущийAsk1!=0&amp;&amp;ТекущийBid1!=0" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ОткрПозиПоРынк17" Category="OpenPosition" Location="1269.3589742166005 1206.9276478208581" TypeName="OpenPositionByMarketItem">
          <EditItem Guid="ef286656-3888-427d-ba51-2887b09061d9" CodeName="ОткрПозиПоРынк17" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="Long" TypeName="Boolean" Value="false" />
              <Parameter Name="Shares" TypeName="Double" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЗакрПозиПоРынк4" Category="ClosePosition" Location="1255.0848417259385 1315.4281771610163" TypeName="ClosePositionByMarketItem">
          <EditItem Guid="a6566477-9199-4f0e-adb5-0277a7dd7e33" CodeName="ЗакрПозиПоРынк4" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="AddOpenName" TypeName="Boolean" Value="false" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ОткрПозиПоРынк10" Category="OpenPosition" Location="1465.3589742166005 1202.9276478208581" TypeName="OpenPositionByMarketItem">
          <EditItem Guid="d447b24f-babd-4378-b28e-4cb66cb98c7d" CodeName="ОткрПозиПоРынк10" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="Long" TypeName="Boolean" Value="true" />
              <Parameter Name="Shares" TypeName="Double" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ЗакрПозиПоРынк5" Category="ClosePosition" Location="1473.0848417259385 1311.4281771610163" TypeName="ClosePositionByMarketItem">
          <EditItem Guid="eee86a34-9f93-4513-ac9d-74029ffeaa85" CodeName="ЗакрПозиПоРынк5" IsParametersVisible="false" OnlyValueHandlersCanUsed="true">
            <Parameters>
              <Parameter Name="Execution" TypeName="PositionExecution" Value="Normal" />
              <Parameter Name="AddOpenName" TypeName="Boolean" Value="false" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="НачальныйBuy2" Category="Const" Location="188.49203953162089 1088.98322242002" TypeName="ConverterItem">
          <EditItem Guid="3ecf4a44-b37b-4080-9acf-3c19e06d771a" CodeName="НачальныйBuy2" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.ConstGen, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="НачальныйSell2" Category="Const" Location="1038.7932053519244 1089.9922138432526" TypeName="ConverterItem">
          <EditItem Guid="104fa729-feab-466a-baed-7a94e61b1417" CodeName="НачальныйSell2" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.ConstGen, TSLab.Script.Handlers, Version=2.1.12.0, Culture=neutral, PublicKeyToken=null" />
        </Block>
        <Block Key="Формула11" Category="Formula" Location="376.73261337335964 937.69311804824281" TypeName="DoubleCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="143" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="b90894af-001d-4416-86ca-80afa4fd7a2c" CodeName="Формула11" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.DoubleCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="ТекущийAsk==0||ТекущийBid==0||ТекущийAsk1==0||ТекущийBid1==0?(Закрытие1/Закрытие2*Вес2)*-НачальныйBuy2:(ТекущийBid/ТекущийAsk1*Вес2)*-НачальныйBuy2" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="Формула12" Category="Formula" Location="1154.8691651629765 929.26229532458467" TypeName="DoubleCustomHandlerItem" Width="120" Height="60" ResizablePartWidth="143" ResizablePartHeight="80" OpenParams="false">
          <EditItem Guid="fe8c824b-51d9-41f4-84b2-12546df7baaf" CodeName="Формула12" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.ScriptEngine.Template.DoubleCustomHandlerItem+Handler, TSLab.ScriptEngine, Version=2.1.13.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Expression" TypeName="String" Value="ТекущийAsk==0||ТекущийBid==0||ТекущийAsk1==0||ТекущийBid1==0?(Закрытие1/Закрытие2*Вес2)*НачальныйSell2:(ТекущийAsk/ТекущийBid1*Вес2)*НачальныйSell2" />
              <Parameter Name="StartIndex" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="ИмпорВещесЗначе" Category="ServiceElements" Location="1.2851122871790608 496.06867546207138" TypeName="ConverterItem">
          <EditItem Guid="db4381ed-d951-4703-a598-e8a9c7248e29" CodeName="ИмпорВещесЗначе" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="TSLab.Script.Handlers.ImportDoubleValuesHandler, TSLab.Script.Handlers, Version=2.1.12.58, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="Id" TypeName="String" Value="LOT" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="_MA_Sell_1" Category="vvAverages_My" Location="1354.6946353254659 387.9034067679807" TypeName="ConverterItem">
          <EditItem Guid="5123f484-6315-489f-8063-59b75593c17f" CodeName="_MA_Sell_1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="vvTSLtools_2_1_My.AllAverages, vvTSLtools_2_1_My, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="MaParam1" TypeName="Double" Value="0" />
              <Parameter Name="MaParam2" TypeName="Double" Value="0" />
              <Parameter Name="MaPeriod2" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="_MA_Sell_0" Category="vvAverages_My" Location="1333.9524947599102 534.98403986919323" TypeName="ConverterItem">
          <EditItem Guid="62a686a2-169b-4057-9e3a-cf58dd333b1b" CodeName="_MA_Sell_0" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="vvTSLtools_2_1_My.AllAverages, vvTSLtools_2_1_My, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="MaParam1" TypeName="Double" Value="0" />
              <Parameter Name="MaParam2" TypeName="Double" Value="0" />
              <Parameter Name="MaPeriod2" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="СвязаннПарамет4" Category="Usual" Location="1518.7529507636475 476.5289164571729" TypeName="ParameterShareItem">
          <EditItem ParameterName1="MAType" ParameterName2="MAType" />
        </Block>
        <Block Key="СвязаннПарамет" Category="Usual" Location="764.36621445688843 516.4756005051413" TypeName="ParameterShareItem">
          <EditItem ParameterName1="MaPeriod" ParameterName2="MaPeriod" />
        </Block>
        <Block Key="СвязаннПарамет5" Category="Usual" Location="781.46413611526168 440.70158275303135" TypeName="ParameterShareItem">
          <EditItem ParameterName1="MAType" ParameterName2="MAType" />
        </Block>
        <Block Key="_MA_Buy" Category="vvAverages_My" Location="619.29146981940323 563.26877700404191" TypeName="ConverterItem">
          <EditItem Guid="3b970f31-9f40-47db-ae86-b6fcfdf97948" CodeName="_MA_Buy" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="vvTSLtools_2_1_My.AllAverages, vvTSLtools_2_1_My, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="MaParam1" TypeName="Double" Value="0" />
              <Parameter Name="MaParam2" TypeName="Double" Value="0" />
              <Parameter Name="MaPeriod2" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="_MA_Buy1" Category="vvAverages_My" Location="598.54932925384753 425.61638961444544" TypeName="ConverterItem">
          <EditItem Guid="b61ee811-7cd1-4391-bd02-d761e7fad1b2" CodeName="_MA_Buy1" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="vvTSLtools_2_1_My.AllAverages, vvTSLtools_2_1_My, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="MaParam1" TypeName="Double" Value="0" />
              <Parameter Name="MaParam2" TypeName="Double" Value="0" />
              <Parameter Name="MaPeriod2" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="_MA_Buy2" Category="vvAverages_My" Location="340.44409847091748 1046.5375540080836" TypeName="ConverterItem">
          <EditItem Guid="6baa8087-30bd-4927-aa06-2cf6a509795d" CodeName="_MA_Buy2" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="vvTSLtools_2_1_My.AllAverages, vvTSLtools_2_1_My, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="MaParam1" TypeName="Double" Value="0" />
              <Parameter Name="MaParam2" TypeName="Double" Value="0" />
              <Parameter Name="MaPeriod2" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="_MA_Buy3" Category="vvAverages_My" Location="336.67280018627105 1140.8200111242456" TypeName="ConverterItem">
          <EditItem Guid="2a1f645b-0ca4-4dd3-ae33-566b40d184bc" CodeName="_MA_Buy3" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="vvTSLtools_2_1_My.AllAverages, vvTSLtools_2_1_My, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="MaParam1" TypeName="Double" Value="0" />
              <Parameter Name="MaParam2" TypeName="Double" Value="0" />
              <Parameter Name="MaPeriod2" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="СвязаннПарамет6" Category="Usual" Location="508.27371219374578 1063.508396288993" TypeName="ParameterShareItem">
          <EditItem ParameterName1="MAType" ParameterName2="MAType" />
        </Block>
        <Block Key="СвязаннПарамет2" Category="Usual" Location="504.37533453163513 1135.5111157564561" TypeName="ParameterShareItem">
          <EditItem ParameterName1="MaPeriod" ParameterName2="MaPeriod" />
        </Block>
        <Block Key="_MA_Sell_2" Category="vvAverages_My" Location="1081.8760465437406 1022.0241151578814" TypeName="ConverterItem">
          <EditItem Guid="a03f3ede-ad45-428a-a7d4-bf89f84663f8" CodeName="_MA_Sell_2" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="vvTSLtools_2_1_My.AllAverages, vvTSLtools_2_1_My, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="MaParam1" TypeName="Double" Value="0" />
              <Parameter Name="MaParam2" TypeName="Double" Value="0" />
              <Parameter Name="MaPeriod2" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="_MA_Sell_3" Category="vvAverages_My" Location="1091.3042922553568 1165.3334499744476" TypeName="ConverterItem">
          <EditItem Guid="1dbbd832-dc4d-41b7-88be-6537d4ac5f7a" CodeName="_MA_Sell_3" IsParametersVisible="false" OnlyValueHandlersCanUsed="false" HandlerTypeName="vvTSLtools_2_1_My.AllAverages, vvTSLtools_2_1_My, Version=1.0.0.0, Culture=neutral, PublicKeyToken=null">
            <Parameters>
              <Parameter Name="MaParam1" TypeName="Double" Value="0" />
              <Parameter Name="MaParam2" TypeName="Double" Value="0" />
              <Parameter Name="MaPeriod2" TypeName="Int32" Value="0" />
            </Parameters>
          </EditItem>
        </Block>
        <Block Key="СвязаннПарамет7" Category="Usual" Location="1264.7908534051548 1037.1093082964674" TypeName="ParameterShareItem">
          <EditItem ParameterName1="MAType" ParameterName2="MAType" />
        </Block>
        <Block Key="СвязаннПарамет3" Category="Usual" Location="1247.6929317467816 1112.8833260485771" TypeName="ParameterShareItem">
          <EditItem ParameterName1="MaPeriod" ParameterName2="MaPeriod" />
        </Block>
        <Link From="Источник1" To="Закрытие1" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <GraphLink From="Источник1" To="Главная" FromPort="Out" ToPort="RIGHT" Category="ChartCandleLink">
          <Data>
            <GraphData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ListStyle="LINE" CandleStyle="BAR_CANDLE" LineStyle="SOLID" Color="-14685179" AltColor="-262137" Opacity="0" HideLastValue="false" Thickness="1" AltThickness="1" PaneSide="RIGHT" Visible="true" ShowTrades="true" CandleFillStyle="Decreasing" Autoscaling="true">
              <Points />
            </GraphData>
          </Data>
        </GraphLink>
        <Link From="Источник2" To="Закрытие2" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <GraphLink From="Источник2" To="Главная1" FromPort="Out" ToPort="RIGHT" Category="ChartCandleLink">
          <Data>
            <GraphData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ListStyle="LINE" CandleStyle="BAR_CANDLE" LineStyle="SOLID" Color="-9020983" AltColor="-15285015" Opacity="0" HideLastValue="false" Thickness="1" AltThickness="1" PaneSide="RIGHT" Visible="true" ShowTrades="true" CandleFillStyle="Decreasing" Autoscaling="true">
              <Points />
            </GraphData>
          </Data>
        </GraphLink>
        <Link From="Источник1" To="ОтноситКомисси" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник2" To="ОтноситКомисси1" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник1" To="ТекущийBid" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник1" To="ТекущийAsk" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник2" To="ТекущийAsk1" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник2" To="ТекущийBid1" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="ТекущийAsk" To="Формула5" FromPort="Out" ToPortNum="0" />
        <Link From="ТекущийBid" To="Формула6" FromPort="Out" ToPortNum="0" />
        <Link From="ТекущийAsk1" To="Формула6" FromPort="Out" ToPortNum="1" />
        <Link From="Формула5" To="Вычесть" FromPort="Out" ToPort="1" ToPortNum="0" />
        <Link From="Формула6" To="Вычесть1" FromPort="Out" ToPort="1" ToPortNum="0" />
        <Link From="НачальныйBuy1" To="Формула7" FromPort="Out" ToPortNum="0" />
        <Link From="НачальныйSell1" To="Формула8" FromPort="Out" ToPortNum="0" />
        <Link From="Источник1" To="Объем" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник2" To="Объем1" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Объем" To="Формула5" FromPort="Out" ToPortNum="0" />
        <Link From="Объем1" To="Формула7" FromPort="Out" ToPortNum="0" />
        <Link From="Объем" To="Формула6" FromPort="Out" ToPortNum="0" />
        <Link From="Объем1" To="Формула8" FromPort="Out" ToPortNum="0" />
        <Link From="ШагЛота" To="Формула3" FromPort="Out" ToPortNum="0" />
        <Link From="ШагЛота1" To="Формула4" FromPort="Out" ToPortNum="0" />
        <Link From="УмножитНа" To="Формула3" FromPort="Out" ToPortNum="1" />
        <Link From="УмножитНа" To="Формула4" FromPort="Out" ToPortNum="1" />
        <Link From="Источник1" To="ШагЛота" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник2" To="ШагЛота1" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник1" To="ОчереЗаявоЦена" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник2" To="ОчереЗаявоЦена1" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <GraphLink From="ОчереЗаявоЦена" To="Главная" FromPort="Out" ToPort="LEFT" Category="ChartLineLink">
          <Data>
            <GraphData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ListStyle="LINE" CandleStyle="BAR_CANDLE" LineStyle="SOLID" Color="-3028913" AltColor="-2446534" Opacity="0" HideLastValue="false" Thickness="1" AltThickness="1" PaneSide="LEFT" Visible="true" ShowTrades="true" CandleFillStyle="Decreasing" Autoscaling="true">
              <Points />
            </GraphData>
          </Data>
        </GraphLink>
        <GraphLink From="ОчереЗаявоЦена1" To="Главная1" FromPort="Out" ToPort="LEFT" Category="ChartLineLink">
          <Data>
            <GraphData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ListStyle="LINE" CandleStyle="BAR_CANDLE" LineStyle="SOLID" Color="-2718088" AltColor="-10919072" Opacity="0" HideLastValue="false" Thickness="1" AltThickness="1" PaneSide="LEFT" Visible="true" ShowTrades="true" CandleFillStyle="Decreasing" Autoscaling="true">
              <Points />
            </GraphData>
          </Data>
        </GraphLink>
        <Link From="Формула10" To="Вычесть2" FromPort="Out" ToPort="1" ToPortNum="0" />
        <Link From="Формула9" To="Вычесть3" FromPort="Out" ToPort="1" ToPortNum="0" />
        <Link From="ТекущийAsk" To="Формула9" FromPort="Out" ToPortNum="0" />
        <Link From="ТекущийAsk" To="Формула10" FromPort="Out" ToPortNum="0" />
        <Link From="ЛогичесФормула2" To="ЗакрПозиПоРынк3" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ЛогичесФормула2" To="ЗакрПозиПоРынк2" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ЛогичесФормула1" To="ЗакрПозиПоРынк1" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ОткрПозиПоРынк14" To="ЗакрПозиПоРынк1" FromPort="Out" ToPort="Pos" ToPortNum="0" />
        <Link From="ОткрПозиПоРынк" To="ЗакрПозиПоРынк" FromPort="Out" ToPort="Pos" ToPortNum="0" />
        <Link From="ЛогичесФормула" To="ОткрПозиПоРынк14" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ЛогичесФормула" To="ОткрПозиПоРынк" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ЛогичесФормула3" To="ОткрПозиПоРынк16" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ЛогичесФормула3" To="ОткрПозиПоРынк9" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="Источник1" To="ОткрПозиПоРынк" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник2" To="ОткрПозиПоРынк14" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник1" To="ОткрПозиПоРынк16" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник2" To="ОткрПозиПоРынк9" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Формула7" To="ЛогичесФормула" FromPort="Out" ToPortNum="0" />
        <Link From="Формула7" To="ЛогичесФормула1" FromPort="Out" ToPortNum="0" />
        <Link From="Формула8" To="ЛогичесФормула3" FromPort="Out" ToPortNum="0" />
        <Link From="Формула8" To="ЛогичесФормула2" FromPort="Out" ToPortNum="0" />
        <Link From="Формула3" To="ОткрПозиПоРынк" FromPort="Out" ToPort="Shares" ToPortNum="2" />
        <Link From="Формула3" To="ОткрПозиПоРынк16" FromPort="Out" ToPort="Shares" ToPortNum="2" />
        <Link From="Формула4" To="ОткрПозиПоРынк9" FromPort="Out" ToPort="Shares" ToPortNum="2" />
        <Link From="ОткрПозиПоРынк9" To="ЗакрПозиПоРынк3" FromPort="Out" ToPort="Pos" ToPortNum="0" />
        <Link From="ОткрПозиПоРынк16" To="ЗакрПозиПоРынк2" FromPort="Out" ToPort="Pos" ToPortNum="0" />
        <Link From="Формула4" To="ОткрПозиПоРынк14" FromPort="Out" ToPort="Shares" ToPortNum="2" />
        <GraphLink From="Формула7" To="Главная2" FromPort="Out" ToPort="RIGHT" Category="ChartLineLink">
          <Data>
            <GraphData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ListStyle="LINE" CandleStyle="BAR_CANDLE" LineStyle="SOLID" Color="-9204258" AltColor="-15363092" Opacity="0" HideLastValue="false" Thickness="1" AltThickness="1" PaneSide="RIGHT" Visible="true" ShowTrades="true" CandleFillStyle="Decreasing" Autoscaling="true">
              <Points />
            </GraphData>
          </Data>
        </GraphLink>
        <GraphLink From="Вычесть" To="Главная2" FromPort="Out" ToPort="RIGHT" Category="ChartLineLink">
          <Data>
            <GraphData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ListStyle="LINE" CandleStyle="BAR_CANDLE" LineStyle="SOLID" Color="-2235126" AltColor="-4104635" Opacity="0" HideLastValue="false" Thickness="1" AltThickness="1" PaneSide="RIGHT" Visible="true" ShowTrades="true" CandleFillStyle="Decreasing" Autoscaling="true">
              <Points />
            </GraphData>
          </Data>
        </GraphLink>
        <GraphLink From="Вычесть3" To="Главная2" FromPort="Out" ToPort="RIGHT" Category="ChartLineLink">
          <Data>
            <GraphData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ListStyle="LINE" CandleStyle="BAR_CANDLE" LineStyle="SOLID" Color="-8177979" AltColor="-7398717" Opacity="0" HideLastValue="false" Thickness="1" AltThickness="1" PaneSide="RIGHT" Visible="true" ShowTrades="true" CandleFillStyle="Decreasing" Autoscaling="true">
              <Points />
            </GraphData>
          </Data>
        </GraphLink>
        <Link From="Формула5" To="Вычесть4" FromPort="Out" ToPort="1" ToPortNum="0" />
        <Link From="Формула9" To="Вычесть5" FromPort="Out" ToPort="1" ToPortNum="0" />
        <Link From="ЛогичесФормула9" To="ОткрПозиПоРынк2" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ЛогичесФормула9" To="ОткрПозиПоРынк18" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ОткрПозиПоРынк2" To="ЗакрПозиПоРынк10" FromPort="Out" ToPort="Pos" ToPortNum="0" />
        <Link From="ОткрПозиПоРынк18" To="ЗакрПозиПоРынк11" FromPort="Out" ToPort="Pos" ToPortNum="0" />
        <Link From="ЛогичесФормула10" To="ЗакрПозиПоРынк10" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ЛогичесФормула10" To="ЗакрПозиПоРынк11" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="Источник1" To="ОткрПозиПоРынк2" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник2" To="ОткрПозиПоРынк18" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Вычесть5" To="ЛогичесФормула10" FromPort="Out" ToPortNum="0" />
        <Link From="Вычесть4" To="ЛогичесФормула9" FromPort="Out" ToPortNum="0" />
        <Link From="ЛогичесФормула4" To="ОткрПозиПоРынк17" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ЛогичесФормула5" To="ЗакрПозиПоРынк4" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ОткрПозиПоРынк17" To="ЗакрПозиПоРынк4" FromPort="Out" ToPort="Pos" ToPortNum="0" />
        <Link From="ЛогичесФормула4" To="ОткрПозиПоРынк10" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ЛогичесФормула5" To="ЗакрПозиПоРынк5" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="ОткрПозиПоРынк10" To="ЗакрПозиПоРынк5" FromPort="Out" ToPort="Pos" ToPortNum="0" />
        <Link From="Источник1" To="ОткрПозиПоРынк17" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Источник2" To="ОткрПозиПоРынк10" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Формула6" To="Вычесть7" FromPort="Out" ToPort="1" ToPortNum="0" />
        <Link From="Формула10" To="Вычесть6" FromPort="Out" ToPort="1" ToPortNum="0" />
        <Link From="Вычесть6" To="ЛогичесФормула5" FromPort="Out" ToPortNum="0" />
        <Link From="Вычесть7" To="ЛогичесФормула4" FromPort="Out" ToPortNum="0" />
        <Link From="ТекущийAsk" To="Формула11" FromPort="Out" ToPortNum="0" />
        <Link From="ТекущийAsk" To="Формула12" FromPort="Out" ToPortNum="0" />
        <Link From="ЛогичесФормула1" To="ЗакрПозиПоРынк" FromPort="Out" ToPort="Eq" ToPortNum="1" />
        <Link From="Формула3" To="ОткрПозиПоРынк2" FromPort="Out" ToPort="Shares" ToPortNum="2" />
        <Link From="Формула3" To="ОткрПозиПоРынк17" FromPort="Out" ToPort="Shares" ToPortNum="2" />
        <Link From="Формула4" To="ОткрПозиПоРынк18" FromPort="Out" ToPort="Shares" ToPortNum="2" />
        <Link From="Формула4" To="ОткрПозиПоРынк10" FromPort="Out" ToPort="Shares" ToPortNum="2" />
        <Link From="Источник1" To="ИмпорВещесЗначе" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <GraphLink From="Вычесть1" To="Главная3" FromPort="Out" ToPort="RIGHT" Category="ChartLineLink">
          <Data>
            <GraphData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ListStyle="LINE" CandleStyle="BAR_CANDLE" LineStyle="SOLID" Color="-6970278" AltColor="-6071161" Opacity="0" HideLastValue="false" Thickness="1" AltThickness="1" PaneSide="RIGHT" Visible="true" ShowTrades="true" CandleFillStyle="Decreasing" Autoscaling="true">
              <Points />
            </GraphData>
          </Data>
        </GraphLink>
        <GraphLink From="Формула8" To="Главная3" FromPort="Out" ToPort="RIGHT" Category="ChartLineLink">
          <Data>
            <GraphData xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" ListStyle="LINE" CandleStyle="BAR_CANDLE" LineStyle="SOLID" Color="-2846675" AltColor="-16212598" Opacity="0" HideLastValue="false" Thickness="1" AltThickness="1" PaneSide="RIGHT" Visible="true" ShowTrades="true" CandleFillStyle="Decreasing" Autoscaling="true">
              <Points />
            </GraphData>
          </Data>
        </GraphLink>
        <Link From="Формула6" To="_MA_Sell_1" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Формула10" To="_MA_Sell_0" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="_MA_Sell_1" To="СвязаннПарамет1" FromPort="Out" ToPort="ScriptEditor.Master" ToPortNum="0" />
        <Link From="_MA_Sell_0" To="СвязаннПарамет1" FromPort="Out" ToPort="ScriptEditor.Slave" ToPortNum="1" />
        <Link From="_MA_Sell_0" To="Вычесть2" FromPort="Out" ToPort="2" ToPortNum="1" />
        <Link From="_MA_Sell_1" To="Вычесть1" FromPort="Out" ToPort="2" ToPortNum="1" />
        <Link From="_MA_Sell_1" To="СвязаннПарамет4" FromPort="Out" ToPort="ScriptEditor.Master" ToPortNum="0" />
        <Link From="_MA_Sell_0" To="СвязаннПарамет4" FromPort="Out" ToPort="ScriptEditor.Slave" ToPortNum="1" />
        <Link From="_MA_Buy" To="СвязаннПарамет5" FromPort="Out" ToPort="ScriptEditor.Slave" ToPortNum="1" />
        <Link From="_MA_Buy" To="СвязаннПарамет" FromPort="Out" ToPort="ScriptEditor.Slave" ToPortNum="1" />
        <Link From="_MA_Buy" To="Вычесть3" FromPort="Out" ToPort="2" ToPortNum="1" />
        <Link From="Формула9" To="_MA_Buy" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="_MA_Buy1" To="СвязаннПарамет5" FromPort="Out" ToPort="ScriptEditor.Master" ToPortNum="0" />
        <Link From="_MA_Buy1" To="Вычесть" FromPort="Out" ToPort="2" ToPortNum="1" />
        <Link From="_MA_Buy1" To="СвязаннПарамет" FromPort="Out" ToPort="ScriptEditor.Master" ToPortNum="0" />
        <Link From="Формула5" To="_MA_Buy1" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="_MA_Buy2" To="СвязаннПарамет6" FromPort="Out" ToPort="ScriptEditor.Master" ToPortNum="0" />
        <Link From="_MA_Buy3" To="СвязаннПарамет6" FromPort="Out" ToPort="ScriptEditor.Slave" ToPortNum="1" />
        <Link From="_MA_Buy2" To="СвязаннПарамет2" FromPort="Out" ToPort="ScriptEditor.Master" ToPortNum="0" />
        <Link From="_MA_Buy3" To="СвязаннПарамет2" FromPort="Out" ToPort="ScriptEditor.Slave" ToPortNum="1" />
        <Link From="_MA_Buy2" To="Вычесть4" FromPort="Out" ToPort="2" ToPortNum="1" />
        <Link From="_MA_Buy3" To="Вычесть5" FromPort="Out" ToPort="2" ToPortNum="1" />
        <Link From="Формула5" To="_MA_Buy2" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Формула9" To="_MA_Buy3" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="НачальныйBuy2" To="Формула11" FromPort="Out" ToPortNum="0" />
        <Link From="Формула11" To="ЛогичесФормула9" FromPort="Out" ToPortNum="0" />
        <Link From="Формула11" To="ЛогичесФормула10" FromPort="Out" ToPortNum="0" />
        <Link From="_MA_Sell_2" To="СвязаннПарамет7" FromPort="Out" ToPort="ScriptEditor.Master" ToPortNum="0" />
        <Link From="_MA_Sell_3" To="СвязаннПарамет7" FromPort="Out" ToPort="ScriptEditor.Slave" ToPortNum="1" />
        <Link From="_MA_Sell_2" To="СвязаннПарамет3" FromPort="Out" ToPort="ScriptEditor.Master" ToPortNum="0" />
        <Link From="_MA_Sell_3" To="СвязаннПарамет3" FromPort="Out" ToPort="ScriptEditor.Slave" ToPortNum="1" />
        <Link From="_MA_Sell_2" To="Вычесть7" FromPort="Out" ToPort="2" ToPortNum="1" />
        <Link From="_MA_Sell_3" To="Вычесть6" FromPort="Out" ToPort="2" ToPortNum="1" />
        <Link From="Формула6" To="_MA_Sell_2" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="Формула10" To="_MA_Sell_3" FromPort="Out" ToPort="Src" ToPortNum="0" />
        <Link From="ИмпорВещесЗначе" To="УмножитНа" FromPort="Out" ToPort="Src" ToPortNum="0" />
      </Model>
    </ViewModel>
  </EditData>
  <Id>931d93b0-da2d-480e-86fc-0dad8e4d535e</Id>
  <Options xsi:type="LabOptions">
    <BarSizes>
      <BarSize Key="" Value="5.6089302673549355" />
      <BarSize Key="Profit" Value="7.7406" />
    </BarSizes>
    <PaneSizes>
      <PaneSize Key="Главная" Value="15.376866414408003" />
      <PaneSize Key="Главная1" Value="27.442157914200557" />
      <PaneSize Key="Главная2" Value="28.742485167848731" />
      <PaneSize Key="Главная3" Value="28.438490503542702" />
      <PaneSize Key="ПанельГрафика" Value="50" />
      <PaneSize Key="Главная4" Value="20.557472189408031" />
    </PaneSizes>
    <Indent>0</Indent>
    <BarsIndent>0</BarsIndent>
    <HideValues>false</HideValues>
    <LegendTransparency>0</LegendTransparency>
    <TimeScale>Adaptive</TimeScale>
    <GroupTrades>true</GroupTrades>
    <LegendForegroundColor>
      <Value>
        <A>0</A>
        <R>0</R>
        <G>0</G>
        <B>0</B>
      </Value>
      <IsChanged>false</IsChanged>
      <Default>
        <A>255</A>
        <R>215</R>
        <G>215</G>
        <B>215</B>
      </Default>
    </LegendForegroundColor>
    <ChartBackgroundColor>
      <Value>
        <A>0</A>
        <R>0</R>
        <G>0</G>
        <B>0</B>
      </Value>
      <IsChanged>false</IsChanged>
      <Default>
        <A>255</A>
        <R>0</R>
        <G>0</G>
        <B>0</B>
      </Default>
    </ChartBackgroundColor>
    <ChartForegroundColor>
      <Value>
        <A>0</A>
        <R>0</R>
        <G>0</G>
        <B>0</B>
      </Value>
      <IsChanged>false</IsChanged>
      <Default>
        <A>255</A>
        <R>255</R>
        <G>255</G>
        <B>255</B>
      </Default>
    </ChartForegroundColor>
    <ChartGridColor>
      <Value>
        <A>0</A>
        <R>0</R>
        <G>0</G>
        <B>0</B>
      </Value>
      <IsChanged>false</IsChanged>
      <Default>
        <A>255</A>
        <R>49</R>
        <G>49</G>
        <B>49</B>
      </Default>
    </ChartGridColor>
    <ChartBorderColor>
      <Value>
        <A>0</A>
        <R>0</R>
        <G>0</G>
        <B>0</B>
      </Value>
      <IsChanged>false</IsChanged>
      <Default>
        <A>255</A>
        <R>49</R>
        <G>49</G>
        <B>49</B>
      </Default>
    </ChartBorderColor>
    <ChartRulerBackgroundColor>
      <Value>
        <A>0</A>
        <R>0</R>
        <G>0</G>
        <B>0</B>
      </Value>
      <IsChanged>false</IsChanged>
      <Default>
        <A>255</A>
        <R>73</R>
        <G>73</G>
        <B>73</B>
      </Default>
    </ChartRulerBackgroundColor>
    <ChartRulerForegroundColor>
      <Value>
        <A>0</A>
        <R>0</R>
        <G>0</G>
        <B>0</B>
      </Value>
      <IsChanged>false</IsChanged>
      <Default>
        <A>255</A>
        <R>255</R>
        <G>255</G>
        <B>255</B>
      </Default>
    </ChartRulerForegroundColor>
    <IntervalBase>MINUTE</IntervalBase>
    <Interval>5</Interval>
    <GraphListVisibilities>
      <GraphListVisibility Key="Buy &amp; Hold" Value="false" />
    </GraphListVisibilities>
    <VerticalScales />
    <RecalcInterval>INTERVAL</RecalcInterval>
    <DateFrom>2021-01-01T00:00:00</DateFrom>
    <UseDateFrom>true</UseDateFrom>
    <DateTo>2021-01-01T00:00:00</DateTo>
    <UseDateTo>false</UseDateTo>
    <DateReload>2021-04-18T21:00:00+00:00</DateReload>
    <UseDateReload>false</UseDateReload>
    <MaxDays>0</MaxDays>
    <SessionBegin>2000-01-01T00:00:00</SessionBegin>
    <SessionEnd>2000-01-01T00:00:00</SessionEnd>
    <DecompressMethod>Method1</DecompressMethod>
    <MaxCandels>100</MaxCandels>
    <RtUpdates>true</RtUpdates>
    <CalcForEachSecurity>false</CalcForEachSecurity>
    <ScriptEditorShowLinks>true</ScriptEditorShowLinks>
    <TradeFromBar>0</TradeFromBar>
    <IsSplittedProfitByInstruments>false</IsSplittedProfitByInstruments>
    <NotUsePositions>false</NotUsePositions>
    <InitDeposit>0</InitDeposit>
    <LabCalcType>Default</LabCalcType>
    <TradeMode>All</TradeMode>
    <IsShowedBlockNumbers>false</IsShowedBlockNumbers>
    <LimitOrderExecutionMode>Touch</LimitOrderExecutionMode>
  </Options>
  <Mappings>
    <Sources>
      <Source DataSourceName="BinanceFutures" SecurityId="ADAUSDT" Name="13E828E4-4633-455C-B81B-730B003D8002" VisualTypeName="Торгуемый инструмент" IsOption="false">
        <Records />
      </Source>
      <Source DataSourceName="BinanceFutures" SecurityId="AVAXUSDT" Name="dae2c52a-3337-4eea-9caf-f302f70848d5" VisualTypeName="Торгуемый инструмент" IsOption="false">
        <Records />
      </Source>
    </Sources>
    <Parameters>
      <Parameter xsi:type="OptimData" ItemName="4a074d54-81cb-4469-bbd7-698000095100" BlockName="НачальныйBuy1" Name="Значение" InvariantName="Value" CodeName="НачальныйBuy1_Value" UsedInOptimization="false" IsCalculable="false" Value="0.024" TypeName="Double" MinValue="0.01" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="OptimData" ItemName="c149f466-7e54-4b9f-b86a-ca97cdda67be" BlockName="НачальныйSell1" Name="Значение" InvariantName="Value" CodeName="НачальныйSell1_Value" UsedInOptimization="false" IsCalculable="false" Value="0.028" TypeName="Double" MinValue="0" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="OptimData" ItemName="3ecf4a44-b37b-4080-9acf-3c19e06d771a" BlockName="НачальныйBuy2" Name="Значение" InvariantName="Value" CodeName="НачальныйBuy2_Value" UsedInOptimization="false" IsCalculable="false" Value="0.02" TypeName="Double" MinValue="0.01" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="OptimData" ItemName="104fa729-feab-466a-baed-7a94e61b1417" BlockName="НачальныйSell2" Name="Значение" InvariantName="Value" CodeName="НачальныйSell2_Value" UsedInOptimization="false" IsCalculable="false" Value="0.014" TypeName="Double" MinValue="0.01" MaxValue="0.07" Step="0.002" ControlMinValue="1" ControlMaxValue="10" ControlStep="1" NumberDecimalDigits="1" />
      <Parameter xsi:type="IntOptimData" ItemName="5123f484-6315-489f-8063-59b75593c17f" BlockName="_MA_Sell_1" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Sell_1_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="50" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="5123f484-6315-489f-8063-59b75593c17f" BlockName="_MA_Sell_1" Name="MAType" InvariantName="MAType" CodeName="_MA_Sell_1_MAType" UsedInOptimization="false" IsCalculable="false" Value="0" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="2f3a13c8-9c42-4cac-90ed-36a8aabe926f" BlockName="_MA_Buy1" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Buy1_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="10" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="2f3a13c8-9c42-4cac-90ed-36a8aabe926f" BlockName="_MA_Buy1" Name="MAType" InvariantName="MAType" CodeName="_MA_Buy1_MAType" UsedInOptimization="false" IsCalculable="false" Value="0" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="6baa8087-30bd-4927-aa06-2cf6a509795d" BlockName="_MA_Buy2" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Buy2_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="10" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="6baa8087-30bd-4927-aa06-2cf6a509795d" BlockName="_MA_Buy2" Name="MAType" InvariantName="MAType" CodeName="_MA_Buy2_MAType" UsedInOptimization="false" IsCalculable="false" Value="0" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="a03f3ede-ad45-428a-a7d4-bf89f84663f8" BlockName="_MA_Sell_2" Name="MaPeriod" InvariantName="MaPeriod" CodeName="_MA_Sell_2_MaPeriod" UsedInOptimization="false" IsCalculable="false" Value="10" TypeName="Int32" MinValue="1" MaxValue="20" Step="1" ControlMinValue="1" ControlMaxValue="20" ControlStep="1" />
      <Parameter xsi:type="IntOptimData" ItemName="a03f3ede-ad45-428a-a7d4-bf89f84663f8" BlockName="_MA_Sell_2" Name="MAType" InvariantName="MAType" CodeName="_MA_Sell_2_MAType" UsedInOptimization="false" IsCalculable="false" Value="0" TypeName="Int32" MinValue="0" MaxValue="25" Step="1" ControlMinValue="0" ControlMaxValue="25" ControlStep="1" />
    </Parameters>
    <ParameterGroups />
    <AutoParameters>
      <AutoParameter xsi:type="OptimData" ItemName="20c0fe4b-ca55-4d52-a705-5f0ed08971c1" Name="АвтоЗначение" InvariantName="AutoProperty" UsedInOptimization="false" IsCalculable="false" Value="0" MinValue="0" MaxValue="0" Step="0" ControlMinValue="0" ControlMaxValue="0" ControlStep="0" NumberDecimalDigits="1" />
    </AutoParameters>
  </Mappings>
  <OptimizationMethodTypeName>BruteForceOptimization</OptimizationMethodTypeName>
  <Iterations>1380</Iterations>
  <OptParametersRecords />
  <OptParametersRecordsFolders />
</GraphDataBase>"""

setting_script = """{"Options":{"DefEntryApprove":true,"DefExitApprove":true,"AutoEntryBars":2,"AutoEntryIgnoreByMarketAsLimit":false,"AutoCloseBars":2,"AutoCloseIgnoreByMarketAsLimit":false,"Slippage":0,"SlippagePct":0.0,"TakeProfitNoSlippage":false,"OpenPositionNoSlippage":false,"ByMarketAsLimt":false,"InvalidStopsByMarket":false,"RemoveInactivePositions":false,"WarnSkippedOpenPositions":false,"NotOpenIfHasSkippedExit":false,"NoCalcInfo":false,"MaxBarsForSignal":2,"ExitSignalOnlyForLastBar":true,"WaitExecutionExitBars":0,"WaitExecutionEntryBars":0,"SimulatePositionOrdering":true,"UseCommissionInProfit":true,"EventOrderRejected":false,"EventOrderFilled":false,"EventOrderCanceled":false,"EventOrderQtyChanged":false,"EventPositionOpening":false,"EventPositionClosing":false,"EventTradingIsStarted":true,"EventTradingIsStopped":false,"EventBarClosedNoTrades":true,"EventPretradeLimitation":false},"Mappings":{"Sources":[],"Parameters":[],"ParameterGroups":[],"AutoParameters":[]},"AppearanceOptions":{"BarSizes":[],"PaneSizes":[],"GraphListVisibilities":[],"VerticalScales":[]},"Layout":null,"AppProperties":{}}"""
setting_agent = """{"Options":{"DefEntryApprove":true,"DefExitApprove":true,"AutoEntryBars":2,"AutoEntryIgnoreByMarketAsLimit":false,"AutoCloseBars":2,"AutoCloseIgnoreByMarketAsLimit":false,"Slippage":0,"SlippagePct":0.0,"TakeProfitNoSlippage":false,"OpenPositionNoSlippage":false,"ByMarketAsLimt":false,"InvalidStopsByMarket":false,"RemoveInactivePositions":false,"WarnSkippedOpenPositions":false,"NotOpenIfHasSkippedExit":false,"NoCalcInfo":false,"MaxBarsForSignal":2,"ExitSignalOnlyForLastBar":true,"WaitExecutionExitBars":0,"WaitExecutionEntryBars":0,"SimulatePositionOrdering":true,"UseCommissionInProfit":true,"EventOrderRejected":false,"EventOrderFilled":false,"EventOrderCanceled":false,"EventOrderQtyChanged":false,"EventPositionOpening":false,"EventPositionClosing":false,"EventTradingIsStarted":true,"EventTradingIsStopped":false,"EventBarClosedNoTrades":true,"EventPretradeLimitation":false},"Mappings":{"Sources":[{"Name":"13E828E4-4633-455C-B81B-730B003D8002","VisualTypeName":"Торгуемый инструмент","IsOption":false,"Records":[],"DataSourceName":"BinanceFutures","SecurityId":"CELRUSDT","IsDefined":true},{"Name":"dae2c52a-3337-4eea-9caf-f302f70848d5","VisualTypeName":"Торгуемый инструмент","IsOption":false,"Records":[],"DataSourceName":"BinanceFutures","SecurityId":"ONEUSDT","IsDefined":true}],"Parameters":[],"ParameterGroups":[],"AutoParameters":[]},"AppearanceOptions":{"BarSizes":[],"PaneSizes":[{"Key":"Главная","Value":15.376866414408003},{"Key":"Главная1","Value":27.442157914200557},{"Key":"Главная2","Value":28.742485167848731},{"Key":"Главная3","Value":28.438490503542702},{"Key":"ПанельГрафика","Value":50.0},{"Key":"Главная4","Value":20.557472189408031}],"GraphListVisibilities":[],"VerticalScales":[]},"AppProperties":{},"Layout":null}"""
