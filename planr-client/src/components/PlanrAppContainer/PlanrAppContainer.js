import React from 'react';

import TopMenuBar from '../TopMenuBar/TopMenuBar';
import DashColumn from '../DashColumn/DashColumn';
import Card from '../Card/Card';
import TextInput from '../form-elements/TextInput/TextInput';
import Button from '../form-elements/Button/Button';

class PlanrAppContainer extends React.Component {

    render() {
        return <div className="PlanrAppContainer w-100 h-screen bg-gray-200 overflow-x-hidden">
            <TopMenuBar />
            <div className="PlanrDashContainer w-screen p-6 flex flex-row  flex-wrap">
                <DashColumn title="Column 1">
                    <Card title="Section A">
                        <ul className="list-disc list-inside">
                            <li>El 1</li>
                            <li>El 2</li>
                            <li>El 3</li>
                            <li>El 4</li>
                            <li>El 5</li>
                        </ul>
                    </Card>
                    <Card title="Section B">
                        <TextInput label="Form Input A"></TextInput>
                        <TextInput label="Form Input B"></TextInput>
                        <Button value="Submit"></Button>
                    </Card>
                </DashColumn>
                <DashColumn title="Column 2">
                    <Card title="Section A">
                        <div className="overflow-hidden truncate min-w-0 w-min break-all">
                            Hello world!
                        </div>
                    </Card>
                </DashColumn>
                <DashColumn title="Column 3">
                    <Card title="Section A">
                        Hello world!
                    </Card>
                </DashColumn>
            </div>
        </div>
    }
}

export default PlanrAppContainer;