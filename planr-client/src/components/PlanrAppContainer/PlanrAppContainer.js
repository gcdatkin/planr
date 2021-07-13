import React from 'react';

import TopMenuBar from '../TopMenuBar/TopMenuBar';
import DashColumn from '../DashColumn/DashColumn';
import Card from '../Card/Card';
import TextInput from '../TextInput/TextInput';
import Button from '../Button/Button';

class PlanrAppContainer extends React.Component {

    render() {
        return <div className="PlanrAppContainer w-screen h-screen bg-gray-200">
            <TopMenuBar />
            <div className="PlanrDashContainer w-screen p-6 flex flex-row content-stretch flex-wrap">
                <DashColumn >
                    <Card title="Test">
                        <ul className="list-disc list-inside">
                            <li>El 1</li>
                            <li>El 2</li>
                            <li>El 3</li>
                            <li>El 4</li>
                            <li>El 5</li>
                        </ul>
                    </Card>
                    <Card title="Test 2">
                        <TextInput></TextInput>
                        <Button></Button>
                    </Card>
                </DashColumn>
                <DashColumn>
                    <Card title="Test">
                        Hello
                    </Card>
                </DashColumn>
                <DashColumn />
            </div>
        </div>
    }
}

export default PlanrAppContainer;